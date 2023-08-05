#!/usr/bin/env python
# Copyright (c) didigo. All rights reserved.
from setuptools import find_packages, setup
import fastmodel.backend.util.file as utils
import os

def recursive_files(base_dir):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(base_dir):
        for filename in filenames:
            file_list.append(os.path.join(dirpath, filename))
    return file_list

setup(
    name='edit-anything',
    version='0.0.2',
    description='EditAnything',
    long_description=utils.get_file_content("README.md"),
    long_description_content_type='text/markdown',
    author='wfbi',
    author_email='myname@example.com',
    keywords='EditAnything',
    url='https://github.com/xxx/xxxx',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
    license='Apache License 2.0',
    install_requires=utils.parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
              'edit-anything=fastmodel.main:main'
          ]
    },
    ext_modules=[],
)
