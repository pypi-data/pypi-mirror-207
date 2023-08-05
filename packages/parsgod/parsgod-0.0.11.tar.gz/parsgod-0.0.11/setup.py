from setuptools import setup
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='parsgod',
    version='0.0.11',
    description='A module for generating the python parser framework',
    author='Alexander554',
    author_email='gaa.280811@gmail.com',
    license='MIT',
    packages=['parsgod'],
    install_requires=[
        'requests',
    ],
    readme="README.md",
    long_description=long_description,
    long_description_content_type='text/markdown',
)