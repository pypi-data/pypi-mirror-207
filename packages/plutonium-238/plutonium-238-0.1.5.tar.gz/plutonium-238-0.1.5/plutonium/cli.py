import json
import os
import argparse
from plutonium.utils import logger, VoyagerDetect
from plutonium.config import (
    VOYAGER_SERVER,
    VOYAGER_USERNAME,
    VOYAGER_PASSWORD,
    VOYAGER_TOKEN,
    GOVERNANCE_TOKEN,
    LOG_FILENAME,
    LOGO
)

def init_parse():
    parser = argparse.ArgumentParser(
        description="SCA Agent based on Cdxgen and internal project Voyager I, for application dependencies and risk discovery。"
    )
    parser.add_argument(
        "-t",
        "--type",
        dest="type",
        required=True,
        help="project/image/package/project_file/image_file/package_file",
    )
    parser.add_argument(
        "-l",
        "--language",
        dest="language",
        default=None,
        help="project language",
    )
    parser.add_argument(
        "--target",
        dest="target",
        help="Source directory or container image or binary file",
    )
    # sca分析参数
    parser.add_argument(
        "--no-error",
        action="store_true",
        default=False,
        dest="noerror",
        help="Continue on error to prevent build from breaking",
    )
    parser.add_argument(
        "--license",
        action="store_true",
        default=False,
        dest="license",
        help="Try to get license",
    )
    parser.add_argument(
        "--deep",
        action="store_true",
        default=False,
        dest="deep_scan",
        help="Perform deep scan by passing this --deep argument to cdxgen. Useful while scanning docker images and OS packages.",
    )
    parser.add_argument(
        "--package_cmd",
        action="store_true",
        default=False,
        help="是否通过包命令解析软件",
    )
    parser.add_argument(
        "--package_file",
        action="store_true",
        default=False,
        help="是否获取包文件数据",
    )
    parser.add_argument(
        "--docker_file",
        action="store_true",
        default=False,
        help="是否获取dockerfile数据",
    )
    # 服务端参数
    parser.add_argument(
        "--voyager-server",
        default=VOYAGER_SERVER,
        dest="voyager_server",
        help="Voyager server url. Eg: https://api.voyager.com",
    )
    parser.add_argument(
        "--voyager-username",
        default=VOYAGER_USERNAME,
        dest="voyager_username",
        help="Voyager username",
    )
    parser.add_argument(
        "--voyager-password",
        default=VOYAGER_PASSWORD,
        dest="voyager_password",
        help="Voyager password",
    )
    parser.add_argument(
        "--voyager-token",
        default=VOYAGER_TOKEN,
        dest="voyager_token",
        help="Voyager token for token based submission",
    )
    parser.add_argument(
        "--governance-token",
        default=GOVERNANCE_TOKEN,
        dest="governance_token",
        help="Governance token for token based submission",
    )
    # 项目参数信息
    parser.add_argument(
        "--project_name",
        help="project name",
    )
    parser.add_argument(
        "--project_repository_url",
        help="project repository url",
    )
    parser.add_argument(
        "--project_user",
        help="project user",
    )
    parser.add_argument(
        "--project_branch",
        help="project branch",
    )
    parser.add_argument(
        "--project_file",
        help="project file",
    )
    parser.add_argument(
        "--project_pod",
        help="project pod",
    )
    parser.add_argument(
        "--project_service_name",
        help="project service name",
    )
    parser.add_argument(
        "--project_commit_id",
        help="project commit id",
    )
    # 镜像参数信息
    parser.add_argument(
        "--image_name",
        help="镜像名称",
    )
    parser.add_argument(
        "--image_file",
        help="镜像文件",
    )
    parser.add_argument(
        "--image_repository_url",
        help="镜像仓库地址",
    )
    parser.add_argument(
        "--internet_reachable",
        action="store_true",
        default=False,
        help="是否能够访问互联网",
    )
    parser.add_argument(
        "--core_application",
        action="store_true",
        default=False,
        help="是否是核心应用",
    )
    parser.add_argument(
        "--deploy_test_env",
        action="store_true",
        default=False,
        help="部署环境为测试环境",
    )
    parser.add_argument(
        "--deploy_pro_env",
        action="store_true",
        default=False,
        help="部署环境为正式环境",
    )
    parser.add_argument(
        "--extra_data",
        help="附加参数a=b&c=d",
    )
    parser.print_help()
    return parser.parse_args()


def main():
    print(LOGO)
    args = init_parse()
    data = {
        'op_type': 'create_project_governance',
        'type': args.type,
        'governance_token': args.governance_token if args.governance_token else GOVERNANCE_TOKEN,
        # 项目信息
        'language': args.language,
        # 镜像类
        'image_name': args.image_name,
        'image_repository_url': args.image_repository_url,
        'internet_reachable': args.internet_reachable,
        'core_application': args.core_application,
        'deploy_test_env': args.deploy_test_env,
        'deploy_pro_env': args.deploy_pro_env,
        # 项目类
        'project_name': args.project_name,
        'project_branch': args.project_branch,
        'project_user': args.project_user,
        'project_commit_id': args.project_commit_id,
        'project_pod': args.project_pod,
        'project_service_name': args.project_service_name,
        'project_repository_url': args.project_repository_url,
        # 附加参数
        'extra_data': args.extra_data,
    }
    attach_files = [
        # 提交的名称前缀需要与scan_log_detail的type一致
        # 项目文件
        # ('attach_file', ('2.md', open('./todo.md', 'rb'),)),
        # ('core_files_list', ('pom.xml', open('./todo.md', 'rb'), )),
        # ('core_files_list', ('package.json.lock', open('./todo.md', 'rb'), )),
        # ('sbom_files_list', ('sca_cdxgen.json', open('./voyager.json', 'rb'),)),
        # ('sbom_files_list', ('sca_dependency_tree.txt', open('./todo.md', 'rb'), )),
        # ('vul_files_list', ('vul_veinmind.json', open('./todo.md', 'rb'), )),
    ]
    detector = VoyagerDetect(
        token=args.voyager_token if args.voyager_token else VOYAGER_TOKEN,
        url=args.voyager_server if args.voyager_server else VOYAGER_SERVER,
        username=args.voyager_username if args.voyager_username else VOYAGER_USERNAME,
        password=args.voyager_password if args.voyager_password else VOYAGER_PASSWORD,
    )
    # 项目安全检测
    if args.type in ['project', 'project_file']:
        # 如果是项目文件
        if args.project_file:
            try:
                attach_files.append(
                    ('attach_file', (args.project_file.split('/')[-1].split('.')[0], open(args.project_file, 'rb'),)),
                )
            except Exception as e:
                logger.error(e)
        else:
            # 需要在项目目录下进行sca分析，并进行结果上传
            sca_data = detector.sca_analysis(language=args.language, src_dir=args.target,
                                               sca_tool=True, package_cmd=args.package_cmd,
                                               package_file=args.package_file,
                                               docker_file=args.docker_file,
                                               deep=args.deep_scan)
            # 获取sca工具获取的sbom文件
            for item in sca_data['sca_tool']:
                try:
                    attach_files.append(
                        ('sbom_files_list', (item['result'].split('/')[-1], open(item['result'], 'rb'),)),
                    )
                except Exception as e:
                    logger.error(e)
            # 逐个遍历命令结果数据
            # 将sbom数据放置到data里
            if args.package_cmd:
                try:
                    data['package_cmd'] = json.dumps(sca_data['package_cmd'])
                except Exception as e:
                    logger.error(e)
            if args.package_file:
                for item in sca_data['package_file']:
                    try:
                        # 名称添加package_file前缀
                        attach_files.append(
                            (
                            'sbom_files_list', ('package_file_'+item.split('/')[-1], open(item, 'rb'),)),
                        )
                    except Exception as e:
                        logger.error(e)
            if args.docker_file:
                for item in sca_data['docker_file']:
                    try:
                        # 名称添加package_file前缀
                        attach_files.append(
                            (
                            'sbom_files_list', ('docker_file_'+item.split('/')[-1], open(item, 'rb'),)),
                        )
                    except Exception as e:
                        logger.error(e)
            
            # 封装运行记录、包文件、通过命令获取的包文件内容
            try:
                attach_files.append(
                    ('core_files_list', (LOG_FILENAME.split('/')[-1], open(LOG_FILENAME, 'rb'),)),
                )
            except Exception as e:
                logger.error(e)
        scan_status = detector.base_scan(data, attach_files)
        print(scan_status)
    # 镜像安全检测
    elif args.type in ['image', 'image_file']:
        if args.image_file:
            try:
                attach_files.append(
                    ('attach_file', (args.image_file.split('/')[-1].split('.')[0], open(args.image_file, 'rb'),)),
                )
            except Exception as e:
                logger.error(e)
        # run_log进行上传
        try:
            attach_files.append(
                ('core_files_list', (LOG_FILENAME, open(LOG_FILENAME, 'rb'),)),
            )
        except Exception as e:
            logger.error(e)
        scan_status = detector.scan(data, attach_files)
        print(scan_status)
    # 软件包检测
    elif args.type in ['package','package_file']:
        pass
    else:
        pass
if __name__ == '__main__':
    main()
