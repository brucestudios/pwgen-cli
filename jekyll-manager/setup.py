from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jekyll-manager",
    version="0.1.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A command-line tool to manage Jekyll sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/jekyll-manager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "jekyll-manager=jekyll_manager.cli:main",
        ],
    },
)