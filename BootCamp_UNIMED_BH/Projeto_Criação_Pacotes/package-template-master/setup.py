from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    
    name="Photo_Album_WilsonMuniz",
    version="0.0.1",
    author="Wilson Muniz Fonseca",
    author_email="pc-wilson@hotmail.com",
    description="O pacote Photo_Album e usado para montar um album de fotos baseado em imagens que são convertidas para o padrão 'pdf'.",
    long_description=page_description,   
    long_description_content_type="text/markdown",
    url="https://github.com/WilsonMuniz/Educacao_Devs.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)    