from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-profile-readme-gen",
    version="0.1.0",
    author="Bruce Fang",
    author_email="henshao.fang@outlook.com",
    description="A tool to generate GitHub profile READMEs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/github-profile-readme-gen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'github-readme-gen=github_profile_readme_gen.cli:main',
        ],
    },
)