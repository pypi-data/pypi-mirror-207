
from setuptools import setup, find_packages

setup(
    name='dogfood-logger',
    version='0.1.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Logger for Grafana',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/dogfoodhq/dogfood-logger',
    author='Matt Wong',
    author_email='nycmattw@gmail.com'
)
