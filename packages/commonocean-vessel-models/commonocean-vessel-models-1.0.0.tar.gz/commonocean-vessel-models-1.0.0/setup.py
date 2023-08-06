from setuptools import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='commonocean-vessel-models',
    version='1.0.0',
    description='Implementation of vessels models with varying abstraction levels.',
    keywords='autonomous automated vessels motion planning',
    url='https://commonocean.cps.cit.tum.de/',
    author='Cyber-Physical Systems Group, Technical University of Munich',
    author_email='commonocean@lists.lrz.de',
    packages=find_packages(exclude=['scripts']),
    long_description_content_type='text/markdown',
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    include_package_data=True,
)
