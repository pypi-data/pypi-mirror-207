from setuptools import setup, find_packages

setup(
    name='solution_harsha',
    version='0.9',
    description='A tool for performing string matching on text files',
    author='Sriharsha Aryasomayajula',
    author_email='harshaarya17@outlook.com',
    packages=find_packages(),
    package_data={"": ["config.yaml"]},
    include_package_data=True,
    install_requires=[
        'ruamel.yaml',
        'regex',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'stringapp_di=solution_harsha.di_testcode:main',
        ],
    },
)