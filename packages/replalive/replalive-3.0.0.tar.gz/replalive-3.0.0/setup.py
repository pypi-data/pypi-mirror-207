from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='replalive',
    version='3.0.0',
    description='Keep your replit project online 24/7!',
    author='Hologramsteve#1900 on discord',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'requests',
    ]
)
#twine upload dist/*