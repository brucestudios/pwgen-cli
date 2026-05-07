from setuptools import setup, find_packages

setup(
    name="openclaw-awesome-cli",
    version="0.1.0",
    author="OpenClaw Agent",
    author_email="agent@openclaw.local",
    description="A command-line tool that prints awesome messages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brucestudios/openclaw-awesome-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'openclaw-awesome=openclaw_awesome_cli.__main__:main',
        ],
    },
)
