"""
A setuptools based setup module
"""
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="lendsmart_autotest",
    version="1.9",
    description="The internal SDK for lendsmart autotest",
    url="https://bitbucket.org/lendsmartlabs/lendsmart_py/",
    # Author details
    author="Lendsmart",
    author_email="infos@lendsmart.ai",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # What does your project relate to?
    keywords="lendsmart autotest",
    packages=find_packages(exclude=["contrib", "tests"]),
    # What do we need for this to run
    install_requires=[
        "selenium==3.141.0",
        "keyboard==0.13.5",
        "pytest==6.0.1",
        "requests==2.24.0",
        "boto3==1.16.28",
        "PyAutoGUI==0.9.50",
        "urllib3",
        "pytest-html==3.1.1",
        "importlib-metadata==4.0.1",
        "Faker==13.15.0",
        "ramda",
        "webdriver_manager",
        "networkx",
    ],
    tests_require=[
        "mock",
    ],
)
