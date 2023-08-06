import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "pqinput",
    version = "0.0.1",
    author = "Lucas Borges",
    author_email = "lucas.borges@fysik.su.se",
    description = ("additional functions for QDng calculations preparations."),
    license = "MIT",
    keywords = "qdng",
    url = "https://gitlab.fysik.su.se/lucas.borges/inputxml",
    packages=setuptools.find_packages(include=['Mdata']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)
