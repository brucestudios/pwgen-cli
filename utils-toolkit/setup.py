from setuptools import setup, find_packages

setup(
    name="utils-toolkit",
    version="0.1.0",
    author="brucestudios",
    author_email="brucestudios@example.com",
    description="A collection of simple utility functions for common tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/utils-toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)