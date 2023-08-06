from setuptools import setup
import setuptools
from src.VersionUtil import VersionUtil

setup(
    name='REMLA23_team12_lib',
    version=VersionUtil.get_version(),
    description='A test library',
    author='Zhiyong Zhu',
    author_email='z13913982280@gmail.com',
    url='https://github.com/remla23-team09/lib',
    license='MIT',
    long_description="fREMLA23_team12_lib",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
)
