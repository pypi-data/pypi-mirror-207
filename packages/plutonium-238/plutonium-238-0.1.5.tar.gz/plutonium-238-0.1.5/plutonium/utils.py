import subprocess
import logging
import os
import sys
import shutil
import requests
import plutonium.config as config
from uuid import uuid4
logger = logging.getLogger(__name__)
formatter = logging.Formatter(config.LOG_FORMAT)
file_handler = logging.FileHandler(config.LOG_FILENAME)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(config.LOG_LEVEL)
# 忽略目录
def filter_ignored_dirs(dirs):
    [
        dirs.remove(d)
        for d in list(dirs)
        if d.lower() in config.ignore_directories or d.startswith(".")
    ]
    return dirs
# 查找python依赖文件
def find_python_reqfiles(path):
    result = []
    req_files = [
        "requirements.txt",
        "Pipfile",
        "poetry.lock",
        "Pipfile.lock",
        "conda.yml",
    ]
    for root, dirs, files in os.walk(path):
        filter_ignored_dirs(dirs)
        for name in req_files:
            if name in files:
                result.append(os.path.join(root, name))
    return result
# 判断是否是二进制字符
def is_binary_string(content):
    textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F})
    return bool(content.translate(None, textchars))
# 判断是否是二进制文件
def is_exe(src):
    if os.path.isfile(src):
        try:
            return is_binary_string(open(src, "rb").read(1024))
        except Exception:
            return False
    return False
# 查找指定后缀文件
def find_files(src, src_ext_name, quick=False, filter=True):
    result = []
    for root, dirs, files in os.walk(src):
        if filter:
            filter_ignored_dirs(dirs)
        for file in files:
            if file == src_ext_name or file.endswith(src_ext_name):
                result.append(os.path.join(root, file))
                if quick:
                    return result
    return result
# 获取路径
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)
# 执行命令
def exec_tool(args, cwd=None, stdout=subprocess.PIPE):
    try:
        logger.debug('Executing "{}"'.format(" ".join(args)))
        if os.environ.get("FETCH_LICENSE"):
            logger.debug(
                "License information would be fetched from the registry. This would take several minutes ..."
            )
        cp = subprocess.run(
            args,
            stdout=stdout,
            stderr=subprocess.STDOUT,
            cwd=cwd,
            env=os.environ.copy(),
            check=False,
            shell=False,
            encoding="utf-8",
        )
        logger.debug(cp.stdout)
        return cp.stdout
    except Exception as e:
        logger.exception(e)
        return str(e)
# 检测项目开发语言
# go/python/java/nodejs
def detect_project_language(src_dir):
    if find_python_reqfiles(src_dir):
        return "python"
    if find_files(src_dir, "pom.xml", quick=True) or find_files(
            src_dir, ".gradle", quick=True
    ):
        return "java"
    if (
            find_files(src_dir, "package.json", quick=True)
            or find_files(src_dir, "yarn.lock", quick=True)
            or find_files(src_dir, "rush.json", quick=True)
    ):
        return "nodejs"
    if find_files(src_dir, "go.sum", quick=True) or find_files(
            src_dir, "Gopkg.lock", quick=True
    ):
        return "go"

    return "other"

# 通过cdxgen来生成sbom
def sca_by_cdxgen(language, bom_file, src_dir=".", deep=False):
    result = {
        'status': False,
        'data': None,
        'message': ''
    }
    cdxgen_cmd = os.environ.get("CDXGEN_CMD", "cdxgen")
    if not shutil.which(cdxgen_cmd):
        local_bin = resource_path(
            os.path.join(
                "local_bin", "cdxgen.exe" if sys.platform == "win32" else "cdxgen"
            )
        )
        if not os.path.exists(local_bin):
            result['message'] = 'command not found'
            return result
        try:
            cdxgen_cmd = local_bin
            # Set the plugins directory as an environment variable
            os.environ["CDXGEN_PLUGINS_DIR"] = resource_path("local_bin")
        except Exception as e:
            result['message'] = e
            return result
    if language:
        sca_args = [cdxgen_cmd, "-r", "-t", language, "-o", bom_file]
    else:
        sca_args = [cdxgen_cmd, "-o", bom_file]
    if deep:
        sca_args.append("--deep")
    sca_args.append(src_dir)
    print(sca_args)
    exec_tool(sca_args, )
    result['status'] = True
    result['data'] = ' '.join(sca_args)
    return result

# 获取sca分析
def get_sca_info(src_dir, language=None, sca_tool=True, package_cmd=True, package_file=True,docker_file=True, deep=False):
    result = {
        'language': '',
        # 通过sca工具分析
        'sca_tool': [],
        # 通过命令读取的结果
        'package_cmd': [],
        # 通过包文件读取
        'package_file': [],
        'docker_file': [],
    }
    if not language:
        language = detect_project_language(src_dir)
    result['language'] = language

    # 1.通过cdxgen来生成
    cdxgen_sbom_file = config.SCA_TOOLS['cdxgen']['sbom_file'].format(uuid4().hex)
    cdxgen_result = sca_by_cdxgen(language, cdxgen_sbom_file, src_dir)
    cdxgen_item = {
        'tool': 'cdxgen',
        'cmd': cdxgen_result['data'],
        'result': cdxgen_sbom_file if cdxgen_result['status'] else cdxgen_result['message']
    }
    result['sca_tool'].append(cdxgen_item)
    
    # 2.通过包列举命令获取包信息
    if package_cmd:
        for i in config.LANG_PACKAGE_CMD[language]:
            # 若不同语言继续有细分，可在此进行各个语言的处理
            if language == 'python':
                try:
                    item = {
                        'cmd': i,
                        'result': None
                    }
                    # 虚拟环境
                    if os.path.exists(src_dir + '/venv'):
                        res = exec_tool((src_dir + '/venv/bin/' + i).split(), cwd=src_dir)
                        item['result'] = res
                    else:
                        res = exec_tool(i.split(), cwd=src_dir)
                        item['result'] = res
                    result['package_cmd'].append(item)
                except Exception as e:
                    logger.error(e)
            else:
                try:
                    item = {
                        'cmd': i,
                        'result': None
                    }
                    res = exec_tool(i.split(), cwd=src_dir)
                    item['result'] = res
                    result['package_cmd'].append(item)
                except Exception as e:
                    logger.error(e)
    # 3.读取依赖文件
    if package_file:
        for i in config.LANG_PACKAGE_FILE[language]:
            if os.path.exists(src_dir + '/' + i):
                logger.info('存在包文件-{}'.format(src_dir + '/' + i))
                result['package_file'].append(src_dir + '/' + i)
    # 4.读取dockerfile
    if docker_file:
        for i in config.DOCKER_FILE_LIST:
            if os.path.exists(src_dir + '/' + i):
                logger.info('存在dockerfile文件-{}'.format(src_dir + '/' + i))
                result['docker_file'].append(src_dir + '/' + i)
    return result

# 基础工具检测
def base_tool_check():
    pass

# 依赖工具安装
def base_tool_install():
    pass


# 服务端检测
class VoyagerDetect():
    def __init__(self, token=None, url=None, username=None, password=None):
        self.api_url = url
        self.api_token = token
        self.api_username = username
        self.api_password = password
        self.req = requests.Session()

    # 1.token生成，token有效期较长，失效后再进行重新生成
    def get_new_token(self):
        try:
            self.req.headers = {}
            res = self.req.post(self.api_url + 'api/member/get-auth-token/',
                                data={'username': self.api_username, 'password': self.api_password})
            token = res.json()['token']
            headers = {
                # 注意Token后有空格
                'Authorization': 'Token ' + token
            }
            self.req.headers = headers
            return token
        except Exception as e:
            logger.error(e)
            return None

    def check_token_valid(self):
        headers = {
            # 注意Token后有空格
            'Authorization': 'Token ' + self.api_token
        }
        self.req.headers = headers
        try:
            res = self.req.get(self.api_url + 'api/member/check-token/', )
            if res.status_code == 200 and res.json()['success']:
                return True
        except Exception as e:
            logger.error(e)
        return False

    # 登录认证
    def login(self):
        login_status = {
            'status': False,
            'message': '',
            'data': None
        }
        if self.api_token:
            if self.check_token_valid():
                login_status['status'] = True
                return login_status
            else:
                # token失效，使用账号密码登录
                login_status['message'] = 'token失效，使用账号密码登录'

        if self.api_username and self.api_password:
            # 获取认证token
            token = self.get_new_token()
            # logger.info(token)
            if token:
                self.api_token = token
                headers = {
                    # 注意Token后有空格
                    'Authorization': 'Token ' + self.api_token
                }
                self.req.headers = headers
                login_status['status'] = True
            else:
                login_status['message'] = '无法生成访问token，账号密码可能错误'
        else:
            login_status['message'] = '请提供API账号以及密码信息'
        logger.info(login_status['message'])
        return login_status

    # sca分析
    def sca_analysis(self, language, src_dir=".", sca_tool=True, package_cmd=True, package_file=True, docker_file=True, deep=False):
        result = get_sca_info(language=language, src_dir=src_dir, sca_tool=sca_tool,
                              package_cmd=package_cmd, package_file=package_file,docker_file=docker_file, deep=deep)
        return result

    # 0.4旧版本的流水线卡点的扫描
    def scan(self, data, files):
        login_status = self.login()
        if login_status['status']:
            if files:
                response = self.req.post(self.api_url + 'api/scan/detect/', data=data, files=files)
            else:
                response = self.req.post(self.api_url + 'api/scan/detect/', data=data, files=[ ('files', ('', None, )),])
            return response.json()
        else:
            return login_status


    # 获取扫描结果或报告
    def get_scan_result(self, task_id):
        login_status = self.login()
        if login_status['status']:
            response = self.req.get(self.api_url + 'api/scan/scan-log/?task_id={}'.format(task_id),)
            return response.json()
        else:
            return login_status
    
    # 新版的与服务端交互
    def base_scan(self, data, files):
        login_status = self.login()
        if login_status['status']:
            if files:
                response = self.req.post(self.api_url + config.VOYAGER_BASE_SCAN_API, data=data, files=files)
            else:
                response = self.req.post(self.api_url + config.VOYAGER_BASE_SCAN_API, data=data, files=[('files', ('', None,)), ])
            return response.json()
        else:
            return login_status['message']
    

    