from setuptools import setup, find_packages
import os
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

setup(
    name='putkoff_chatGPT_API',
    version='0.1.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        # Add your module dependencies here
    ],
    entry_points={
        'console_scripts': [
            'putkoff_chatGPT_API = putkoff_chatGPT_API.main_module:main',
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name="putkoff_chatGPT_API",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="PUTKOFF",
    author_email="putkey2@sbcglobal.net",
    description="`putkoff_chatGPT_API` is a Python module for interacting with OpenAI's GPT models. It simplifies the process of making API calls, managing API keys, and parsing responses, while also providing utility functions to work with timestamps and organize response data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/putkoff_chatGPT_API",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
