#!/usr/bin/env python
from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text()

setup_info = dict(
  name='{NAME}',
  python_requires=">=3.10",
  version='{VERSION}',
  description='{DESCRIPTION}',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="{AUTHOR}",
  author_email='{EMAIL}',
  url='{URL}',
  packages=find_packages(
    where='.', 
    include=['{NAME}*']
  ),
  include_package_data=True,
  install_requires=[],
  setup_requires=[],
  tests_require=['pytest']
)

setup(**setup_info)