from setuptools import setup, find_packages

setup(
    name="hello-world-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple CLI that prints a greeting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/hello-world-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hello-world=hello_world.cli:main',
        ],
    },
)