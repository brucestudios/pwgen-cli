from setuptools import setup, find_packages

setup(
    name="file-sorter-cli",
    version="1.0.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A CLI tool to organize files into folders by type",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/file-sorter",
    packages=[],
    py_modules=["file_sorter"],
    entry_points={
        "console_scripts": [
            "file-sorter=file_sorter:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)