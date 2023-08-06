#!/usr/bin/env python
from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text()

setup_info = dict(
    name='pyboil',
    python_requires=">=3.10",
    version='1.0.0',
    description='CLI script to initialize python packages',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Reed Schick",
    author_email='rns350@nyu.edu',
    url='https://github.com/rns350/pyinit',
    packages=find_packages(
        where='.', 
        include=['pyboil*']
    ),
    include_package_data=True,
    entry_points={
            'console_scripts': [
                'pyboil = pyboil.pyboil:launch',
            ]
        },
    install_requires=[],
    setup_requires=[],
    tests_require=['pytest']
)

setup(**setup_info)