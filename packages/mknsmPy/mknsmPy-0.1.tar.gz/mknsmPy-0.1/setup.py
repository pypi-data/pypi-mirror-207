from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name                          = "mknsmPy", 
    license                       = "MIT",
    version                       = "0.1", 
    packages                      = find_packages(), 
    author                        = "hihimamu", 
    author_email                  = "mamu.pypi@shchiba.uk", 
    url                           = "https://github.com/hihimamuLab/MekanismCalcLibrary.git", 
    description                   = "mekanism material calculator", 
    long_description              = long_description,
    long_description_content_type = "text/x-rst",
    keywords                      = ["mekanism", "mechanism", "mknsm","mknsmPy"]
)
