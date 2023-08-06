from setuptools import setup, find_packages

setup(
    name='sqlflat',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sqlflat = sqlflat.parser:main',
        ],
    },
    install_requires=[
        'regex>=2022.2.22',
    ],
    author='Timothee Desurmont',
    author_email='timothee.desurmont@sampaguitas.com',
    description='A utility for converting SQL queries to a single line format',
    license='MIT',
    url='https://github.com/Sampaguitas/sqlflat',
)
