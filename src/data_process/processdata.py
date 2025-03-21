"""
模块功能：
将langchain文件类型的list进行数据清洗
返回为文件或langchain_core.documents.Document的list

使用示例：
# # 读进来pdf,txt,md文件
# loaders = load_content("raw/")

# loader = loaders[5:7]
# clean_data = cleanData(loader)
# print(clean_data[1].metadata)   

输入：
langchain文件类型的list

输出：
langchain_core.documents.Document的list

"""
from data_process.loader import load_content 
from utils.path_utils import *
from langchain_core.documents import Document
import re
import os

def cleanData(loaders, store_method='list'):
    def clean_text(file_doc):
        pattern = re.compile(r'[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]', re.DOTALL)
        content = file_doc.page_content
        content = re.sub(pattern, lambda match: match.group(0).replace('\n', ''), content) 
        content = content.replace('•', '')
        content = content.replace(' ', '')
        content = content.replace('\n\n', '\n')
        return content
    
    # 可选择清洗结果存在为文件、列表、结构化数据
    
    
    # 若结果存为文档则设置输出路径（默认到data文件下）
    if store_method == 'file':
        out_path = get_data_dir() / "processed"
        os.mkdir(out_path)
        
        for idx, loader in enumerate(loaders):
            docs = loader.load()
            article_content = ""
            for doc in docs:
                doc.page_content = clean_text(doc)
                article_content += doc.page_content + '\n'
            # 生成文件名
            file_name = os.path.join(out_path, f"articel_{idx + 1}.txt")
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(article_content.strip())
        return
    
    
    # 若结果为列表为后续搭建向量数据库使用
    if store_method == 'list':
        clean_articles = []
        # 遍历每个篇文章
        for idx, loader in enumerate(loaders):
            # 遍历每一篇文章的每一页
            docs = loader.load()
            article_content = ""
            metadata = docs[0].metadata
            for doc in docs:
                doc.page_content = clean_text(doc)
                # 合并页面内容
                article_content += doc.page_content + '\n' # split
            # 还原为Document类型
            clean_articles.append(
                Document(
                    page_content=article_content.strip(),
                    metadata=metadata,
                ))
        return clean_articles
            
            
        