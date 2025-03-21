# setup.py
from setuptools import setup, find_packages

setup(
    name="rag_project",
    version="0.1",
    # 关键配置：定义包结构和路径
    packages=find_packages(where="src"),  # 从 src 目录查找所有包
    package_dir={"": "src"}, # 将包根目录设置为src. # 这样在不同包中导入包时只需要 使用包名而不用加src.
)