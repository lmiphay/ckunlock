# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='ckunlock',
      version='0.1.0',
      description='unlock console kit sessions',
      license='GPL-2',
      author='Paul Healy',
      url='https://github.com/lmiphay/ckunlock',
      packages=[
          'ckunlock'
      ],
      install_requires=['invoke'],
      entry_points={
        'console_scripts': ['ckunlock = ckunlock.main:program']
      }
)
