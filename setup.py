from setuptools import setup
import sys


with open("README.md", "r") as f:
    long_desc = f.read()

with open("dry_spell_rwr/version.py") as f:
    exec(f.read())


setup(
    name="dry_spell_rwr",
    version=__version__,
    description="A package for analysing the land surface response to dry spells.",
    long_description=long_desc,
    long_description_content_type="text/markdown",

    url="https://github.com/ppharris/dry_spell_rwr",

    author="Phil Harris, Belen Gallego-Elvira",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Natural Language :: English",

        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",

        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Hydrology",
    ],

    packages=["dry_spell_rwr", ],

    package_data={
        "dry_spell_rwr": ["data/*.nc"],
    },

    install_requires=[
        "cartopy",
        "cftime",
        # conda: cython>0.15.0,
        # conda: cf-units>2,
        # conda: geos (not the pip package!)
        "netcdf4",
        # conda: numpy>1.14,
        # conda: proj,
        # conda: pyke,
        "scipy",
        "scitools-iris",
        # conda: udunits2,
    ],

    python_requires=">=3",
)
