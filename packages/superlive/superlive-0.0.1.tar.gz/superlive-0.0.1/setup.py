import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

NAME = "Superlive"
VERSION = "0.0.1"
PACKAGE_NAME = 'superlive'
AUTHOR = "DR-Tech"
AUTHOR_EMAIL = "dev@dr-tech.co"
SHORT_DESCRIPTION = "Superlive Streaming Host"
URL = 'https://github.com/sophatahsher/superlive_sdk_python'
LICENSE = 'DR-Tech License 2.0'
DESCRIPTION = "Superlive Python SDK"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = []
with open(HERE/"requirements.txt") as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        INSTALL_REQUIRES.append(line)

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    keywords=["Superlive"],
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "superlive"},
    packages=find_packages(where="superlive", exclude=['tests']),# will return a list ['src',]
)



