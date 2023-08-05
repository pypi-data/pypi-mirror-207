from setuptools import setup, find_packages

# README.mdまたはREADME.rstファイルの内容を読み込む
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pymaibool',
    version='0.1.2',
    packages=find_packages(),

    long_description=long_description,
    long_description_content_type="text/markdown",
)