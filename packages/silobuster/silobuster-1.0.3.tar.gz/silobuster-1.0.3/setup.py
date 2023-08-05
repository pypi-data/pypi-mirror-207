from setuptools import setup

desc = '''
A package to manage data. This package provides means to connect to different data sources and transform the data using Pandas. The focus of the library is to canonicalize data sources.

This project is focused on Human Resources data and working with data in various formats. Dedupe.io's machine learning library is used to cluster various data.

Please visit our documentation at https://openreferral.github.io/silobuster-model-trainer/ to learn more.
'''
setup(
    name='silobuster',
    author="Jamey Harris",
    author_email="jameycharris@yahoo.com",
    description=desc,
    url="https://openreferral.github.io/silobuster-model-trainer/",
    include_package_data=True,
    packages=[
        'silobuster', 
        
    ],
    version='1.0.3',
    package_dir={'silobuster': 'silobuster'},
    package_data={'': ['*.*']},
    install_requires=[
        'XlsxWriter>=3.0.7',
        'numpy>=1.21.5',
        'pandas>=1.4.4',
        'pandas-dedupe>=1.5.0',
        'Django>=4.1.5',
        'djangorestframework>=3.14.0',
        'psycopg2>=2.9.3',
        'requests>=2.25.1',
    ],
)

