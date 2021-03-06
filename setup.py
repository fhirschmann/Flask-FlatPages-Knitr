from os import path
from setuptools import setup


setup(
    name="Flask-FlatPages-Knitr",
    version="0.3.1",
    description="Knitr preprocessing for Flask-FlatPages",
    long_description=open(path.join(path.dirname(__file__), "README.rst")).read(),
    url="http://github.com/fhirschmann/Flask-FlatPages-Knitr",
    author="Fabian Hirschmann",
    author_email="fabian@hirschmann.email",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
    platforms="any",
    include_package_data=True,
    install_requires=[
        "Flask",
        #"Flask-FlatPages>=0.6",
        "rpy2"
    ],
    keywords="flask flatpages knitr markdown",
    packages=["flask_flatpages_knitr"],
)
