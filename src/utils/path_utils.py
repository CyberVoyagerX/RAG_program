from pathlib import Path

def get_project_root():
    """
    获取项目根目录(rag/)
    当前目录在/rag/src/utils/path_utils.py
    """
    current_file = Path(__file__).resolve()
    return current_file.parent.parent.parent
def get_data_dir():
    return get_project_root() / "data"

def get_vector_store_dir():
    return get_project_root() / "vactor_store"