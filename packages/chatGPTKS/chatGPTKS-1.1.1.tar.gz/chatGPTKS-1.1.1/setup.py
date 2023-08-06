"""
@Name: setup.py
@Auth: MyName
@Date: 2023/5/9-15:09
@Desc: 用来打包chatGPTKS
@Ver : 0.0.0
"""

from setuptools import setup
packages = ['chatGPTKS']# 唯一的包名，自己取名
setup(
    name='chatGPTKS',  # 包名
    version='1.1.1',  # 版本
    description='这个包对api进行了封装，供公司内部使用',  # 描述
    author='HuntingGame',  # 作者
    author_email='',  # 作者邮箱
    packages=packages # 需要封装的所有包
)
