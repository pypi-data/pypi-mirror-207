from setuptools import setup, find_packages

setup(
    name='bambooai',
    version='0.0.7',
    description='A lightweight library for working with pandas dataframes using natural language queries',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pandas',
        'termcolor',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)