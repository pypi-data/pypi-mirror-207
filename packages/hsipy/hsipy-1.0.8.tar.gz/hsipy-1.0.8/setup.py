import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.8' 
PACKAGE_NAME = 'hsipy' 
AUTHOR = 'Bruno Schuty Teske'
AUTHOR_EMAIL = 'schutyb@schutyb.com'
URL = 'https://github.com/schutyb'

LICENSE = 'bsd-3-clause'
DESCRIPTION = 'Python Module to do Hypespectral Imaging Analysis using the Phasor Transform'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
