import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "canvas_client",
    version = "0.0.1",
    author = "Sanskrut Corp",
    author_email = "dev_team@sanskrut.in",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "Client for Canvas",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=['canvas_client'],
    long_description=read('README.md'),
    install_requires=['requests>=1.0.0', 'six>=1.0.0', 'pyopenssl>=0.15'],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)