from setuptools import find_packages, setup
from typing import list
HYPEN_E_DOT='-e .'
def get_requriment(file_path:str)->list[str]:
    '''
    this function will return the list of requriment
    '''
    requriment=[]
    with open(file_path) as file_obj:
       requriment=file_obj.readlines()
       requriment=[req.replace("\n","") for req in requriment]

       if HYPEN_E_DOT in requriment:
           requriment.remove(HYPEN_E_DOT)
    return requriment


       

setup(name='mlproject',version='0.0.1',author='Vivek',author_email='gangvivek94@gmail.com',
    packages=find_packages(),
    install_requries=get_requriment('requriment.txt')
    )