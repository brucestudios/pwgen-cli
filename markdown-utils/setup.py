from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="markdown-utils",
    version="0.1.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A collection of utilities for processing Markdown files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/markdown-utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
