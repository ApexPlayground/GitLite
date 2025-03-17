from setuptools import setup

setup(name = 'gitlite',
      version = '1.0',
      packages = ['gitlite'],
      entry_points = {
          'console_scripts' : ['gitlite = gitlite.cli:main']
      }
      )