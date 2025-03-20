from dotenv import load_dotenv
from src.utils.path_utils import *
import os

def load_env(env=None):
    """
    根据环境加载.env文件
    :param env:环境名(main)
    """
    env_path = os.path.join(get_project_root(), 'config', '.env')
    
    load_dotenv(env_path)
    
def get_env(Api_name, default=None):
    """
    获取环境变量
    :Api_name: 目标API名
    :return: 获取API内容
    """
    return os.getenv(Api_name, default)