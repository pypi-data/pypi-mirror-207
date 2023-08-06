from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='geocodeus',
    version='22.0',
    description="A Python package for converting US zip codes to latitude and longitude",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sam Mathew',
    author_email='sammathew000@gmail.com',
    install_requires=[
        ''
    ],
    py_modules=['geocodeus']
)
