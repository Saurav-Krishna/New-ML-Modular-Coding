# importing dependies 
from setuptools import setup,find_packages
from typing import List

# creating variables t obe passd in the setup description
PROJECT_NAME = "ML project"
VERSION = "0.0.1"
AUTHOR = "SAURAV KRISHNA"
DESCRIPTION = "Linear Regression"
AUTHOR_EMAIL  = "DbYzK@example.com"

REQUIREMENTS = 'requirements.txt'
# requirement .text -> open -> read -> operation 

def get_requirements()->List[str]:
    with open(REQUIREMENTS) as requirements_file:
        req_list = requirements_file.readlines()
        req_list = [req.replace("\n","") for req in req_list]
        
        if "-e ." in req_list:
            req_list.remove("-e .")  # created whenever the setup.py is run
        
        return req_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires=get_requirements()
    ) 