import os
from uuid import uuid4
import logging
import tempfile
LOGO = r"""
   ,-------------------------------------------------------------------------------.
   |                                                                               |
   |                                                                               |
   |       ____  _       _              _                   ____  _____  ___       |
   |      |  _ \| |_   _| |_ ___  _ __ (_)_   _ _ __ ___   |___ \|___ / ( _ )      |
   |      | |_) | | | | | __/ _ \| '_ \| | | | | '_ ` _ \    __) | |_ \ / _ \      |
   |      |  __/| | |_| | || (_) | | | | | |_| | | | | | |  / __/ ___) | (_) |     |
   |      |_|   |_|\__,_|\__\___/|_| |_|_|\__,_|_| |_| |_| |_____|____/ \___/      |
   |                                                                               |
   |                                                                               |
   |                                                             version 0.1.4     |
   |                                                                               |
   |                 This is a SCA Agent, Copyright@Plutonium Team                 |
   |                                                                               |
   |                                                                               |
   `-------------------------------------------------------------------------------'
"""
# 结果轮询最大时间
RESULT_CHECK_INTERVAL = 1
RESULT_CHECK_TIME_MAX = 1 * 10
# 结果轮询最大次数
RESULT_CHECK_COUNT = 20

# DATA_DIR = os.path.dirname(os.path.abspath(__file__)) +'/data/'
VOYAGER_SERVER = os.getenv('VOYAGER_SERVER') if os.getenv('VOYAGER_SERVER') else 'http://localhost:9999/'
VOYAGER_USERNAME = os.getenv('VOYAGER_USERNAME') if os.getenv('VOYAGER_USERNAME') else 'dev'
VOYAGER_PASSWORD = os.getenv('VOYAGER_PASSWORD') if os.getenv('VOYAGER_PASSWORD') else 'dev'
VOYAGER_TOKEN = os.getenv('VOYAGER_TOKEN') if os.getenv('VOYAGER_TOKEN') else 'x'
GOVERNANCE_TOKEN = os.getenv('GOVERNANCE_TOKEN') if os.getenv('GOVERNANCE_TOKEN') else 'x'

# 默认忽略的目录
ignore_directories = [
    ".git",
    ".svn",
    ".mvn",
    ".idea",
    "dist",
    "bin",
    "obj",
    "backup",
    "docs",
    "tests",
    "test",
    "tmp",
    "report",
    "reports",
    "node_modules",
    ".terraform",
    ".serverless",
    "venv",
    "examples",
    "tutorials",
    "samples",
    "migrations",
    "db_migrations",
    "unittests",
    "unittests_legacy",
    "stubs",
    "mock",
    "mocks",
]

TEMP_DIR = tempfile.gettempdir()
if not TEMP_DIR:
    TEMP_DIR = './tmp/'
SCA_DATA_DIR = TEMP_DIR + '/' + 'plutonium/'
if not os.path.exists(SCA_DATA_DIR):
    try:
        os.makedirs(SCA_DATA_DIR)
    except Exception as e:
        print(e)
        SCA_DATA_DIR = './'

# 日志配置
if os.getenv("DEBUG"):
    LOG_LEVEL = logging.DEBUG
else:
    LOG_LEVEL = logging.INFO
LOG_FILENAME = SCA_DATA_DIR + 'plutonium_run_{}.log'.format(uuid4().hex)
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s  - %(lineno)d - %(message)s'
SCA_TOOLS = {
    'cdxgen': {
        'description': 'cdxgen tool',
        'sbom_file': SCA_DATA_DIR + 'cdxgen_{}.json'
    }
}
LANG_PKG_TYPES = {
    "python": "pypi",
    "java": "maven",
    "jvm": "maven",
    "groovy": "maven",
    "kotlin": "maven",
    "scala": "maven",
    "js": "npm",
    "javascript": "npm",
    "nodejs": "npm",
    "go": "golang",
    "golang": "golang",
    "ruby": "gem",
    "php": "composer",
    "dotnet": "nuget",
    "csharp": "nuget",
    "rust": "cargo",
    "dart": "pub",
    "cpp": "conan",
    "clojure": "clojars",
    "haskell": "hackage",
    "elixir": "hex",
    "github actions": "github",
    "github": "github",
}
LANG_PACKAGE_FILE = {
    "python": ['requirements.txt', 'Pipfile.lock', 'poetry.lock'],
    "java": ["pom.xml", "build.gradle"],
    "nodejs": ["package.json", "package-json.lock", "yarn.lock"],
    "go": ["go.mod", "go.sum", "Gopkg.lock"],
    "other": []
}
LANG_PACKAGE_CMD = {
    "python": ['pip freeze'],
    "java": ['mvn dependency:tree'],
    "nodejs": ['npm list', 'yarn list'],
    "go": ['go list -json -m all'],
    "other": []
}
DOCKER_FILE_LIST = [
    'Dockerfile', 'dockerfile', 'docker-compose.yaml', 
]
# Voyager Server API
# 基础检测API
VOYAGER_BASE_SCAN_API = '/api/scan/base-detect/'
