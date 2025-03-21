"""
模块功能：
减少其他包或模块使用路径时的混乱，使用pathlib对当前项目关键目录整合

使用示例：
data_path = get_data_dir()
直接返回RAG_program/data

返回路径类型：
返回项目根目录：get_project_root : Pathlib
返回数据库目录：get_data_dir :str
返回向量数据库目录：get_vector_store_dir :str
"""
from pathlib import Path

def get_project_root():
    """
    获取项目根目录(rag/)
    当前目录在/rag/src/utils/path_utils.py
    """
    current_file = Path(__file__).resolve()
    return current_file.parent.parent.parent
def get_data_dir():
    data_dir = get_project_root() / "data"
    data_dir.mkdir(exist_ok=True)
    return str(data_dir)

def get_vector_store_dir():
    vector_dir = get_project_root() / get_data_dir() / "vector_store"
    vector_dir.mkdir(exist_ok=True)
    return str(vector_dir)