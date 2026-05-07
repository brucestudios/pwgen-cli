from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jekyll-frontmatter-checker",
    version="0.1.0",
    author="OpenClaw Assistant",
    author_email="example@example.com",
    description="A utility to check Jekyll markdown files for proper frontmatter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/jekyll-frontmatter-checker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyYAML>=5.4',
    ],
    entry_points={
        'console_scripts': [
            'jekyll-check=jekyll_frontmatter_checker.check:main',
        ],
    },
)