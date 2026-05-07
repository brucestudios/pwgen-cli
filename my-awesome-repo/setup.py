from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="awesome-text-utils",
    version="0.1.0",
    author="brucestudios",
    author_email="bruce@example.com",
    description="A lightweight Python library for common text processing utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/awesome-text-utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)