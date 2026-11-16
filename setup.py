# -*- coding: utf-8 -*-
"""Installer for the collective.autoscaling package."""

from setuptools import setup


long_description = (
    open("README.md").read()
    + "\n"
    + open("CONTRIBUTORS.md").read()
    + "\n"
    + open("CHANGES.md").read()
    + "\n"
)


setup(
    name="collective.autoscaling",
    version="2.0.0.dev0",
    description="Automatic scaling of (too large) images in Plone sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Laurent Lasudry",
    author_email="laurent.lasudry@affinitic.be",
    url="https://pypi.python.org/pypi/collective.autoscaling",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "plone.api >= 1.4.11",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
