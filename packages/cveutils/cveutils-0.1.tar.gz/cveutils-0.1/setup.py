from setuptools import setup

setup(
    name='cveutils',
    version='0.1',
    description='This library provides functionality for fetching and parsing information about Common Vulnerabilities and Exposures (CVE) using the NIST National Vulnerability Database (NVD) RESTful API.',
    author='Vinicius Pereira (big0us)',
    author_email='vini@cius.xyz',
    packages=['cveutils'],
    install_requires=[
        'requests',
    ],
)