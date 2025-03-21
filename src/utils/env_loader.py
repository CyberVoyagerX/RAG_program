"""
模块介绍：
该模块可以加载环境变量和获取环境变量中的ApiKey
使用时直接调用get_env + 环境变量中对应APIkey的名字即可直接加载/RAG_program/config/.env文件中的Apikey
在使用前需要创建好对应目录

使用示例：
当前/RAG_program/config/.env的APIkey名为ZHIPUAI_API_KEY
api_key = get_env("ZHIPUAI_API_KEY")

返回内容：
str类型的APIkey

待开发内容：
支持多种APIkey
"""
from dotenv import load_dotenv
from utils.path_utils import *
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
    load_env()
    return os.getenv(Api_name, default)