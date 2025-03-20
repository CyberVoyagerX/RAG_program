from src.data_process.loader import load_content 
import re
# 读进来pdf,txt,md文件
loaders = load_content("raw/")
# 加载数据
# pdf = loaders[0].load()
# print(pdf[0].page_content)
def cleanData(loaders):
    def clean_text(file_doc):
        pattern = re.compile(r'[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]', re.DOTALL)
        content = file_doc.page_content
        content = re.sub(pattern, lambda match: match.group(0).replace('\n', ''), content) 
        content = content.replace('•', '')
        content = content.replace(' ', '')
        content = content.replace('\n\n', '\n')
        return content
    # 遍历每个篇文章
    i, j = 0,0
    for loader in loaders:
        # 遍历每一篇文章的每一页
        docs = loader.load()
        for doc in docs:
            doc.page_content = clean_text(doc)
            
        