from setuptools import setup

setup(
    name='interlo',
    version='0.1',
    description='A package for creating interstellar object ',
    py_modules=['interlo'],
    install_requires=[
        'numpy',
        'matplotlib',
        'astropy',
        'galpy'
    ],
    entry_points='''
        [console_scripts]
        interlo=interlo:main
    ''',
)