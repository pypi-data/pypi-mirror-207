# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:18:31 2023

@author: Tomson
"""
from setuptools import setup

setup(
    author="Tomson Reuters",
    name='vector-marketdata',
    version='1.0.0',
    py_modules=['database_test'],
    install_requires=[
        'pandas==1.5.3',
        'PyMySQL==1.0.3',
        'pytz==2022.7',
        'requests==2.30.0',
        'schedule==1.1.0',
        'setuptools==65.6.3'
    ],
    entry_points={
        'console_scripts': [
            'database_test=database_test:main'
        ]
    }
)
