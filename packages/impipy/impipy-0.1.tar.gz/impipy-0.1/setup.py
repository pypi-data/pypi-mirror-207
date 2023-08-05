from setuptools import setup

setup(
    name='impipy',
    version='0.1',
    description='This library provides tools for calculating feature importance in machine learning models.',
    author='My Name',
    install_requires=['numpy==1.22.3',
                      'pandas==1.4.2',
                      'matplotlib==3.5.1',
                      'seaborn==0.11.2',
                      'scikit-learn==1.1.3',
                      'tqdm==4.64.0'
                      ]
)