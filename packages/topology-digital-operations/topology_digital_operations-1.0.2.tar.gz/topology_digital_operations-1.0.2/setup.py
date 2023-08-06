from setuptools import setup, find_packages

setup(
    name='topology_digital_operations',
    version='1.0.2',
    url='https://github.com/ksantana97',
    author='Karim Jerez',
    author_email='ksantana97@gmail.com',
    description='library for making some operations in digital homotopy theory',
    packages=find_packages(),    
    install_requires=[
        'matplotlib>=3.5.2',
        'numpy>=1.21.5',
        ],
)