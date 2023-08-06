from distutils.core import setup
from setuptools import find_packages

setup(
    name='SpaGoG',
    packages=find_packages(),
    version='0.12',
    license='MIT',
    description='Sparse data classification using Graph of Graphs models',
    author='Shachar Hananya',
    author_email='shacharhananya@gmail.com',
    url='https://github.com/HananyaS/SpaGoG',
    download_url='https://github.com/HananyaS/SpaGoG/archive/refs/tags/v_0.12.tar.gz',
    keywords=["GoG"],
    install_requires=[
        'pandas',
        'torch',
        'torch_geometric',
    ],
)
