from setuptools import setup, find_packages

setup(
    name="temperature-converter",
    version="0.1.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A simple command-line utility to convert temperatures between Celsius and Fahrenheit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/temperature-converter",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "tempconv=src.tempconv.cli:main",
        ],
    },
)