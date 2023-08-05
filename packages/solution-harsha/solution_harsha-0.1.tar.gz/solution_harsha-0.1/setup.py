from setuptools import setup, find_packages

setup(
    name='solution_harsha',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ruamel.yaml',
    ],
    entry_points={
        'console_scripts': [
            'stringapp=solution_harsha.di_testcode:main',
        ],
    },
)