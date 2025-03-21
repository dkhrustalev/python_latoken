from setuptools import find_packages, setup


with open("README.rst", "r") as desc:
    long_description = desc.read()

setup(
    name = 'python_latoken',
    packages = find_packages(include = ['latoken']),
    version = '0.1.0',
    description = 'LATOKEN REST API and STOMP Websocket python implementation',
    long_description = long_description,
    long_description_content_type = "text/x-rst",
    author = 'Nikita Oleinik',
    license = 'MIT',
    url = 'https://github.com/purveyor97/python_latoken',
    install_requires = ['requests', 'stomper', 'websockets'],
    keywords = 'latoken exchange rest websockets api crypto bitcoin trading',
    classifiers = [
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)