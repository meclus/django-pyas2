# -*- coding: utf-8 -*-
import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.md')) as f:
    README = f.read()

install_requires = [
    'pyas2lib==1.1.0',
    'django>=1.10.0',
    'requests'
]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-django',
    'coverage',
    'mock'
]


setup(
    name='django-pyas2',
    version='1.0.1',
    description='A Django app for transferring files using AS2 protocol',
    license="GNU GPL v3.0",
    long_description=README,
    author='Abhishek Ram',
    author_email='abhishek8816@gmail.com',
    url='http://github.com/abhishek-ram/django-pyas2',
    packages=['pyas2'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Security :: Cryptography",
        "Topic :: Communications",
    ],
    install_requires=install_requires,
    tests_require=tests_require,
)
