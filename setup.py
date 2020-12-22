import os
from setuptools import setup

setup(
    name = "gaffils",
    version = "0.0.0",
    author = "Ryan S. DeFever",
    author_email = "rdefever@nd.edu",
    description = ("GAFF-based IL force field"),
    entry_points={
        "foyer.forcefields": [
            "load_GAFFILS = gaffils.gaffils:load_GAFFILS",
        ],
    },
)
