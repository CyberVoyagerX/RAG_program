from langchain_community.vectorstores import Chroma
from embedding.zhipu_embedding import ZhipuAIEmbeddings
from utils.path_utils import get_vector_store_dir

def retriever_from_vdb(query, num_vector):
    v_db_path = get_vector_store_dir()
    embedding = ZhipuAIEmbeddings()
    
    vector_db = Chroma(
        persist_directory=v_db_path,
        embedding_function=embedding
    )
    
    return vector_db.max_marginal_relevance_search(query, k=num_vector)


