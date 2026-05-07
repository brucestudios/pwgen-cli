"""Setup configuration for awesome-cli-tool."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="awesome-cli-tool",
    version="0.1.0",
    author="OpenClaw Assistant",
    author_email="assistant@openclaw.dev",
    description="A high-quality command-line interface template in Python for text processing utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/awesome-cli-tool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies required for basic functionality
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "isort>=5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "awesome-text=awesome_cli.cli:main",
        ],
    },
    keywords="cli, text-processing, utility, command-line",
    project_urls={
        "Bug Tracker": "https://github.com/brucestudios/awesome-cli-tool/issues",
        "Documentation": "https://github.com/brucestudios/awesome-cli-tool#readme",
        "Source Code": "https://github.com/brucestudios/awesome-cli-tool",
    },
)