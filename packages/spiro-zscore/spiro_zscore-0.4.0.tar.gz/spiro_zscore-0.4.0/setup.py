#!/usr/bin/env python

import setuptools

from spiro_zscore.version import __version__

LONG_DESCRIPTION = "see https://github.com/valroy/spiro-zscore/README.md"

setuptools.setup(
    name="spiro_zscore",
    author="Valérie Roy",
    author_email="valerie.roy@minesparis.psl.eu",
    description="A z-score calculator for spirometric measurements",
    license="CC BY-SA 4.0",
    keywords=["z-score", "zscore", "spirometry", "fev1", "fvc", "fef"],
    packages=[ "spiro_zscore"],
    version=__version__,
    python_requires=">=3.9",
    package_data={
        'spiro_zscore': [
            'tables/spiro-zscore-lookup.csv',
        ]
    },
    install_requires = ['pandas'],
    tests_require = ['sas7bdat-converter'],
    project_urls = {
        'source': "https://github.com/valroy/spiro-zscore",
    },
)
