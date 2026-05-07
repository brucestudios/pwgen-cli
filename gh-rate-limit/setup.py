from setuptools import setup, find_packages

setup(
    name="gh-rate-limit",
    version="1.0.0",
    author="brucestudios",
    author_email="brucestudios@example.com",
    description="A command-line tool to check GitHub API rate limit status",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/gh-rate-limit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gh-rate-limit=ghratelimit.__main__:main',
        ],
    },
)