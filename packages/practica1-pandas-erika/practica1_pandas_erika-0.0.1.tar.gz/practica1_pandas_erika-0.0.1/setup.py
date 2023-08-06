import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'practica1_pandas_erika'
AUTHOR = 'García Márquez Erika Araceli'
AUTHOR_EMAIL = 'erika_gm1@tesch.edu.mx'
URL = 'https://github.com/Erika-Marquez15/pandas.git'

LICENSE = 'MIT'
DESCRIPTION = 'Es la Practica 1 del segundo parcial en Topicos Avanzados de programación'

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
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