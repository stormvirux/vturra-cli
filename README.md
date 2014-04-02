vturra-cli
==========
[![Build Status](https://travis-ci.org/stormvirux/vturra.svg?branch=master)](https://travis-ci.org/stormvirux/vturra)


Command line Interface for vturra that retrieves result from vtu and analyzes it.

Pre-Requesities
----------------
The following packages should be installed using the operating system packet manager for `linux`. These packages are required for compiling and building `numpy` and `scipy`.

- libatlas-base-dev 
- liblapack-dev 
- gfortran

For Windows `libatlas-base-dev` and `liblapack-dev` are available at [ATLAS](http://math-atlas.sourceforge.net/) and [LAPACK](http://www.netlib.org/lapack/) websites.You can follow this [guide](http://icl.cs.utk.edu/lapack-for-windows/lapack/#running).



`numpy`,`scipy` and `pandas` take quite time to build and install. So instaed of installing the above pre-requesites installing the packages `python-scipy`,`python-numpy` directly using the operating system packet manager would reduce the compile,build time and it will satisfy the above dependencies.

Installation
-------------
Run `python setup.py install` from the package directory `vturra`

Execution
----------
`vturra [year] [stream]`

For example
-----------

`vturra 11 cs` would retrieve the results of `computer science` stream of year `2011`  
