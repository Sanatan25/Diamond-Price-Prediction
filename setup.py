from setuptools import find_packages,setup
from typing import  List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [i.replace("\n","")  for i in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements




setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Sanatan',
    author_email='sanatansenapati25@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)