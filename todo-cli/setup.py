from setuptools import setup, find_packages

setup(
    name="todo-cli",
    version="0.1.0",
    author="brucestudios",
    author_email="example@example.com",
    description="A simple command-line todo list manager",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/todo-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'todo=todo.__main__:main',
        ],
    },
)