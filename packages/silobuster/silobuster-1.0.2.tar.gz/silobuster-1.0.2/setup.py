from setuptools import setup

setup(
    name='silobuster',
    author="Jamey Harris",
    author_email="jameycharris@yahoo.com",
    url="https://openreferral.github.io/silobuster-model-trainer/",
    include_package_data=True,
    packages=[
        'silobuster', 
        
    ],
    version='1.0.2',
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

