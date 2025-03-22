from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, Runnable
from langchain_core.output_parsers import StrOutputParser
from embedding.zhipu_embedding import ZhipuAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from utils.path_utils import get_vector_store_dir
# from retriever import retriever
from utils.env_loader import get_env
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

api_key = get_env("ZHIPUAI_API_KEY")
model = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key=api_key,
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

vector_db = Chroma(
    persist_directory=get_vector_store_dir(),
    embedding_function=ZhipuAIEmbeddings(),
)

template = """
使用下文内容来回答问题，不知道则直接回答不知道，不要试图编造答案。最多使用三句话，答案简明扼要。总在回答的最后说"谢谢你的提问！"。
{context}
问题:{question}
"""

QA_CHAIN_PROMPT=PromptTemplate(input_variables=["context", "question"], template=template)

# 加载检索器
qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vector_db.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

result = qa_chain({"query":"什么是大模型"})

print(result["result"])