#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as history_file:
    history = history_file.read()

requirements = [
    "bottleneck>=1.3.1",
    "cartopy",
    "cftime",
    "cf-xarray>=0.6.1",
    "cftime>=1.4.1",
    "dask[array]>=2.6",
    "geopandas",
    "h5netcdf",
    "intake-xarray>=0.6.1",
    "jsonpickle",
    "numba",
    "numpy>=1.16",
    "pandas>=0.23",
    "pint>=0.10",
    "pyarrow",
    "pyyaml",
    "s3fs>=2022.7.0",
    "scipy>=1.2",
    "xarray>=0.17",
    "xclim>=0.37",
    "zarr>=2.11.1"    
    ]

test_requirements = ['pytest>=3', ]

setup(
    author="Thomas-Charles Fortier Filion",
    author_email='tcff_hydro@outlook.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Hydrology analysis build with xarray",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='xhydro',
    name='xhydro',
    packages=find_packages(include=['xhydro', 'xhydro.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/TC-FF/xhydro',
    version='0.1.2',
    zip_safe=False,
)
