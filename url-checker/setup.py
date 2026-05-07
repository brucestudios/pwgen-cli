from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="url-checker-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to check the status of URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/url-checker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "url-checker=url_checker:main",
        ],
    },
)