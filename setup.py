from os import path
from setuptools import setup


setup(
    name="Flask-FlatPages-Knitr",
    version="0.1",
    description="Knitr rendering for Flask-FlatPages",
    long_description=open(path.join(path.dirname(__file__), "README.rst")).read(),
    url="http://github.com/fhirschmann/Flask-FlatPages-Knitr",
    author="Fabian Hirschmann",
    author_email="fabian@hirschm.net",
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
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    platforms="any",
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-FlatPages",
        "rpy2"
    ],
    keywords="flask flatpages knitr markdown",
    packages=["flask_flatpages_knitr"],
)
