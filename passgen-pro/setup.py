from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="passgen-pro",
    version="1.0.0",
    author="Bruce Studios",
    author_email="bruce@example.com",
    description="A modern, flexible password generator CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/passgen-pro",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'passgen=passgen_pro.cli:main',
        ],
    },
)