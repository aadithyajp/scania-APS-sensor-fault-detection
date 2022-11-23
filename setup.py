from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function wil return list of requirements
    '''
    requirement_list:List[str]=[]
    #code
    with open("requirements.txt","r") as f:
        t = f.read()
        t.append(requirement_list)
        
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="aadithyajp",
    author_email="aadithyajp@gmail.com",
    packages= find_packages(),
    install_requires=[],
)