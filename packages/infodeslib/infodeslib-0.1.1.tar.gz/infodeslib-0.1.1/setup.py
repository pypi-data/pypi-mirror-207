from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'DES with Late Fusion'
LONG_DESCRIPTION = 'Implementation of Dynamic Ensemble Selection methods with Late Fusion'

setup(
    name="infodeslib",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='adv-panda',
    author_email='panda@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='infodeslib',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)