"""
模块功能：
切分langchain.documents.Document类型文档
返回切分组

将处理好的列表文章变为持久化向量保存
使用Chroma向量数据库

使用示例：
loaders = load_content("raw/")
loader = loaders[3:]
clean_data = cleanData(loader)
# print(data.page_content)
split_docs = CutDocument(clean_data)
embedding = ZhipuAIEmbeddings()

vector_db = vertorization(split_docs, embedding)
print(f"向量库中存储的数量：{vector_db._collection.count()}")

question="什么是大语言模型"

    
sim_docs = vector_db.similarity_search(question,k=6)
print(f"检索到的内容数：{len(sim_docs)}")
for i, sim_doc in enumerate(sim_docs):
    print(f"检索到的第{i}个内容: \n{sim_doc.page_content[:200]}", end="\n--------------\n")


文档切分输入：
loader模块中返回的langchain文件list

文档切分输出：
所有切分输出

向量化输入：
文档切分的输出

向量化的输出：
一个持久化的Chroma类型
"""
from utils.path_utils import *
from langchain.vectorstores.chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from data_process.processdata import *
from embedding.zhipu_embedding import ZhipuAIEmbeddings

def CutDocument(text):
    # 切分文档
    text_splitor = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    splited_docs = text_splitor.split_documents(text)
    
    return splited_docs
# 定义持久化保存路径
def vertorization(split_doc, embedding):
    persis_directory = get_vector_store_dir()
    vector_db = Chroma.from_documents(
        documents=split_doc,
        embedding=embedding,
        persist_directory=persis_directory,
    )
    vector_db.persist()
    return vector_db

