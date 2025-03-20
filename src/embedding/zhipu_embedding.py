from src.utils.env_loader import load_env, get_env
from zhipuai import ZhipuAI
# 加载.env文件
load_env()

def zhipu_embedding(text: str):
    """
    根据用户传入文字调用智普编码模型返回文本embedding
    :param text: 需要编码文本
    :reutrn : 返回的embedding
    """
    api_key = get_env("ZHIPUAI_API_KEY")
    client = ZhipuAI(api_key=api_key)
    response = client.embeddings.create(
        model="embedding-3",
        input=text
    )
    return response
