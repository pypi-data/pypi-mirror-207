from setuptools import setup, find_packages

setup(
    name="darwinpyspark",
    version="0.0.1",
    author="Harry Hands",
    author_email="harry.hands@v7labs.com",
    description="A package for interacting with the V7 platform via Pyspark",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/v7labs/darwinpyspark",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[
        "requests"
    ]
)