from setuptools import setup, find_packages
 

 
setup(
  name='venakatest',
  version='0.1.11',
  description='Package used to run tests',
  
  packages=find_packages(),
  install_requires=['PyYAML','requests'] 
)