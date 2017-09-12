# encoding: utf-8
from distutils.core import setup

setup(
    name='german_normalize',
    version='1.1',
    author='Jonas Haag',
    author_email='jonas@lophus.org',
    url='https://github.com/jonashaag/german-normalize',
    license='WTFPL',
    description='Normalize ä ö ü ß -> a(e) o(e) u(e) ss (DIN 5007)',
    py_modules=['german_normalize'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ])
