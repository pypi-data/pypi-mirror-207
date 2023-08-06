import setuptools

from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    
    long_description = fh.read()


setuptools.setup(
    name="qsolve",
    version="0.2.8",
    url = "https://github.com/jfmennemann/qsolve",
    author="Jan-Frederik Mennemann",
    author_email="jfmennemann@gmx.de",
    description="Numerical methods for the simulation of ultracold atom experiments",
    # long_description=read('README.md'),
    long_description=long_description,
    # long_description_content_type='text/markdown',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # package_dir={"": "qsolve"},
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    # package_data={'': ['/qsolve/qsolve/core/*.pyc']},
    # license="MIT",
    keywords="ultracold atoms, classical fields simulations, Gross-Pitaevskii equation, thermal state sampling, time of flight"
)

