from setuptools import setup, find_packages

setup(
    name="hello-world-py",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="A simple Python package that prints a friendly greeting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/hello-world-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)