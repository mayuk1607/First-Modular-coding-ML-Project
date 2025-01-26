#Importing required packages for the setup files
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_req(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = "First Modular ML Project",
    version= '0.0.1',
    author = 'Mayuk Majumder',
    author_email= 'Mayuk1607@gmail.com',
    packages=find_packages(), #Tracks any folder with '__init__.py' file
    install_requires = get_req('requirements.txt')
)

