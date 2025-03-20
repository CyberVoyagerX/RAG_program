"""
模块功能：将指定目录下的所有文件读入，并组织为不同的lanchain格式，交由数据清洗模块进行清洗
模块输入：指定文件目录
模块返回：不同的langchain格式的内容
"""
import os
import re
from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredFileLoader, UnstructuredMarkdownLoader
from src.utils.path_utils import *

# loader = PyMuPDFLoader("rag/llm-universe/data_base/knowledge_db/pumkin_book/pumpkin_book.pdf")

# pdf_pages = loader.load()


def load_content(file_path):
    """
    从指定路径下加载所有文件的目录
    :param 指定目录
    :return :所有文件目录列表
    """
    loaders = []
    file_path = os.path.join(get_data_dir(),file_path)
    for root, dirs, files in os.walk(file_path):
        for file in files:
            # 寻找当前绝对目录
            current_file_path = os.path.join(root, file)
            file_base_name = os.path.basename(current_file_path)
            _, file_type = os.path.splitext(file_base_name)
            file_type = file_type.lower()
            if file_type == '.pdf':
                print(current_file_path)
                loaders.append(PyMuPDFLoader(current_file_path))
            elif file_type == '.md':
                print(current_file_path)
                # 过滤文件，过滤文件名含机密的文件
                pattern = r"机密"
                match = re.search(pattern, file_base_name)
                if not match:
                    loaders.append(UnstructuredMarkdownLoader(current_file_path))
            elif file_type == '.txt':
                print(current_file_path)
                loaders.append(UnstructuredFileLoader(current_file_path))
    
    return loaders

loaders = load_content("raw/")
mdpages = loaders[5].load()
print(type(mdpages))