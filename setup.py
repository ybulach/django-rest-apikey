#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name = 'django_rest_apikey',
	description = 'Per-user API key to authenticate in Django REST Framework',
	version = '0.1',
	license = 'LGPL',
	author = 'Yamine BULACH',
	author_email = 'contact@yamine-bulach.eu',
	url = 'https://github.com/ybulach/django-rest-apikey',
	packages = [
		'django_rest_apikey',
		'django_rest_apikey.migrations'
	],
	install_requires = ['djangorestframework']
)
