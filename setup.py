from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='python-osm/',
      version=version,
      description="OSM Api",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='OpenStreetMap',
      author='Francisco Herrero',
      author_email='francisco.herrero@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
