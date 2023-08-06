from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

setup(
    name="lr3_Serializer",
    version="1.0.0",
    description="Serialization library",
    url="https://github.com/StrawberryAttacks/IGI",
    author="StrawberryAttacks",
    author_email="flufflepuffxx@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True
)
