from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='sqlflat',
    version='1.0.1',
    description='A utility for converting SQL queries to a single line format',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/Sampaguitas/sqlflat',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'sqlflat = sqlflat.parser:main',
        ],
    },
    install_requires=[
        'regex>=2022.2.22',
    ],
    python_requires=">=3.6",
    author='Timothee Desurmont',
    author_email='timothee.desurmont@sampaguitas.com',
    license='MIT',
)
