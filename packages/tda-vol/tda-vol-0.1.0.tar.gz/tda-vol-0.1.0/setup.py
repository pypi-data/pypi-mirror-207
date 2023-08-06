from setuptools import setup, find_packages

setup(
    name='tda-vol',
    version='0.1.0',
    author='Ben Adelman',
    author_email='benadelman2006@gmail.com',
    description='Uses TD Ameritrades API in order to analyze stock/option data. Primarly deals with implied volatility (IV).',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'tda-api',
        'scipy',
        'matplotlib'
    ],
)
