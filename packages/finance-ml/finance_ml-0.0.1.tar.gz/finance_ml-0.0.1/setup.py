from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Application of Machine Learning in Finances'
LONG_DESCRIPTION = 'A package that allows you to build pipelines and evaluate trading strategies, resulting in instructions to operate in the market.'

# Setting up
setup(
    name="finance_ml",
    version=VERSION,
    author="Fabio Maia",
    author_email="<fabio.masaracchia@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'matplotlib'],
    keywords=['python', 'finance', 'mlops'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)