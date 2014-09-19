"""SIMA: Python package for sequential image analysis.
Developed by Patrick Kaifosh, Jeffrey Zaremba, Nathan Danielson.
Copyright (C) 2014 The Trustees of Columbia University in the City of New York.
Licensed under the GNU GPL version 2 or later.
Documentation: http://www.losonczylab.org/sima
Version 0.3.0"""
print __doc__

from sima.imaging import ImagingDataset
from sima.sequence import Sequence

from numpy.testing import Tester
test = Tester().test

__version__ = '0.3.0'
