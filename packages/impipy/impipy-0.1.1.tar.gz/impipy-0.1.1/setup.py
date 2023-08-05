from setuptools import setup
from os import path

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='impipy',
    version='0.1.1',
    description='This library provides tools for calculating feature importance in machine learning models.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Witali Bułatow',
    packages=['impipy'],
    install_requires=['numpy==1.22.3',
                      'pandas==1.4.2',
                      'matplotlib==3.5.1',
                      'seaborn==0.11.2',
                      'scikit-learn==1.1.3',
                      'tqdm==4.64.0'
                      ]
)