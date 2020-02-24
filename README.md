## Dry Spells

A Python package for analysing the land surface response to dry spells.

This package is a set of helper routines for running the dry spell land surface
temperature analysis described in,

Gallego-Elvira, B., C.M. Taylor, P.P. Harris, and D. Ghent (2019), _Evaluation
of Regional‐Scale Soil Moisture‐Surface Flux Dynamics in Earth System Models
Based on Satellite Observations of Land Surface Temperature_,
Geophys. Res. Lett., 46, 5480-5488,
doi:[10.1029/2019GL082962](https://doi.org/10.1029/2019GL082962)

Gallego-Elvira, B., C.M. Taylor, P.P. Harris, D. Ghent, K.L. Veal, and
S.S. Folwell (2016), _Global observational diagnosis of soil moisture control on
the land surface energy balance_,  Geophys. Res. Lett., 43, 2623-2631,
doi:[10.1002/2016GL068178](http://doi.org/10.1002/2016GL068178)

Folwell, S.S., P.P. Harris, and C.M. Taylor (2015), _Large-scale surface
responses during European dry spells diagnosed from land surface temperature_,
J. Hydrometeorol.,
doi:[10.1175/JHM-D-15-0064.1](http://doi.org/10.1175/JHM-D-15-0064.1)


## How to install

If you are installing the package from this source using `setuptools` there are
prerequisites listed below that must be satisfied prior to running,

    python setup.py install


## Requirements

This package requires Python 3 (versions up to 3.7); Python 2 is not supported.
This package uses Cartopy, which has several dependencies that cannot be
satisfied through `setuptools`, so must be available prior to running the
installation.  These are `cython` (version 0.15.1 or later), `numpy` (version
1.14 or later), `udunits2`, `cf-units` (version 2 or later), `proj4` (versions
prior to 6) and `pyke`.
