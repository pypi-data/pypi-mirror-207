# encoding:utf-8
from setuptools import setup, find_packages
import re
from os import path


def read(*paths):
    filename = path.join(path.abspath(path.dirname(__file__)), *paths)
    with open(filename, 'rb') as f:
        return f.read().decode('utf8')


def find_version(*paths):
    contents = read(*paths)
    match = re.search(r'^__version__ = [\'"]([^\'"]+)[\'"]', contents, re.M)
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='dtsdk',
    version=find_version('dtsdk', 'sdk.py'),
    description='DataTower.ai SDK for Python',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/lovinjoy/datatower.ai-python',
    license='Apache',
    author='DataTower.ai, Inc.',
    author_email='contact@lovinjoy.com',
    packages=find_packages(),
    platforms=["all"],
    install_requires=['requests'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)
