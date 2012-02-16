import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pytest-oerp',
    license='Affero GPL 3',
    description='pytest plugin to test OpenERP modules',
    long_description=read("README.rst"),
    version='0.2.0',
    author='Leonardo Santagada',
    author_email='santagada@gmail.com',
    url='http://github.com/santagada/pytest-oerp/',
    py_modules=['pytest_oerp'],
    entry_points={'pytest11': ['oerp = pytest_oerp']},
    install_requires=['pytest>=2.0', 'mock>=0.7'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ]
)
