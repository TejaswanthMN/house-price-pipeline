from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath: str)-> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)

    return requirements


setup(name = 'Regressor-Project',
version = '0.0.1',
author = 'Tejaswanth',
author_email = 'mucheli.n.tejaswanth1@gmail.com',
packages = find_packages(),
install_requires = 'requirements.txt'
)