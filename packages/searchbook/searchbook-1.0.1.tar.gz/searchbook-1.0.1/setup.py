import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.1'
PACKAGE_NAME = 'searchbook'
AUTHOR = 'Alan Reynoso Jacuinde'
AUTHOR_EMAIL = 'alanelhendakari@gmail.com'
URL = 'https://www.instagram.com/aw.jacuxx/'

LICENSE = 'MIT'
DESCRIPTION = 'Libreria que busca un libro mediante ISBN de un archivo CSV'

INSTALL_REQUIRES = [
    'pandas'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
