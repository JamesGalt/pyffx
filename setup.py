from setuptools import setup, find_packages

import sys

with open('README.rst') as f:
    description = f.read()

setup(
    name='pyffx',
    url='http://github.com/JamesGalt/pyffx/',
    version='0.2.1',
    packages=find_packages(),
    license=u'MIT License',
    author=u'Johannes Dollinger',
    description=u'pure Python format preserving encryption',
    long_description=description,
    install_requires=[
        'six',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
