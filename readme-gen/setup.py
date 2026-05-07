from setuptools import setup, find_packages

setup(
    name="readme-gen",
    version="1.0.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A tool to generate professional README.md files for GitHub projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/readme-gen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'readme-gen=readme_gen:main',
        ],
    },
)