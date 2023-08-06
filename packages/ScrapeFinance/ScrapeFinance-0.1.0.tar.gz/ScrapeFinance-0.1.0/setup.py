from setuptools import setup, find_packages

setup(
    name='ScrapeFinance',
    version='0.1.0',
    author='frank',
    author_email='henrywongb@hotmail.com',
    description='dry martini,shaken,not stirred',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/raymond57p/ScrapeFinance',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
    ],
)