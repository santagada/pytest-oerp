from setuptools import setup
setup(
    name='pytest-oerp',
    license='Affero GPL 3',
    description='pytest plugin to test OpenERP modules',
    long_description=open("README.rst").read(),
    version='0.1',
    author='Leonardo Santagada',
    author_email='santagada@gmail.com',
    url='http://github.com/santagada/pytest-oerp/',
    py_modules=['pytest_oerp'],
    entry_points={'pytest11': ['oerp = pytest_oerp']},
    install_requires=['pytest>=2.0', 'mock>=0.7'],
)
