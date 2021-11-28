# -*- coding: utf-8 -*-

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fh:
    readme = fh.read()

setup(
    name='django-activity-log',
    version='0.0.26',
    author='leonidpodriz',
    author_email='leonidpodriz@gmail.com',

    include_package_data=True,
    packages=[
        'activity_log',
        'activity_log.migrations',
    ],

    url='https://github.com/leonidpodriz/django-user-activity-log/',
    license='MIT license',
    description='HTTP queries logger with flexible filters.',
    long_description=readme,
    long_description_content_type="text/markdown",

    install_requires=[
    ],

    classifiers=(
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
