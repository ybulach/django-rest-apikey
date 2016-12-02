#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name = 'django_rest_apikey',
	description = 'Per-user API key to authenticate in Django REST Framework',
	version = '0.1.0',
	license = 'LGPL',
	author = 'Yamine BULACH',
	author_email = 'contact@yamine-bulach.eu',
	url = 'https://github.com/ybulach/django-rest-apikey',
	packages = [
		'django_rest_apikey',
		'django_rest_apikey.migrations'
	],
	install_requires = ['djangorestframework'],
	classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ],
)
