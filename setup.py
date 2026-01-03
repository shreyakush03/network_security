from setuptools import find_packages,setup
from typing import List 

def get_requirements()->List[str]:
    """
      This function will return list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines form the line
            lines=file.readlines()
            #Process each lines
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirement.txt file not found')

    return requirement_list
# print(get_requirements())  #['python-dotenv', 'pandas', 'numpy']

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shreya kushwaha",
    author_email="shreyakush013@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)