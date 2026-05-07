from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="csv-toolkit",
    version="0.1.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A toolkit for CSV file operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/csv-toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'csv-tool=csv_toolkit.cli:main',
        ],
    },
)