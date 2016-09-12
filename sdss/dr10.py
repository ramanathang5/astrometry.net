from __future__ import absolute_import
# This file is part of the Astrometry.net suite.
# Licensed under a 3-clause BSD style license - see LICENSE
import os
try:
    import pyfits
except ImportError:
    try:
        from astropy.io import fits as pyfits
    except ImportError:
        raise ImportError("Cannot import either pyfits or astropy.io.fits")
from astrometry.util.fits import fits_table
import numpy as np

from .common import *
from .dr9 import *

class DR10(DR9):

    def __init__(self, **kwargs):
        '''
        Useful kwargs:
        
        basedir : (string) - local directory where data will be stored.
        '''
        super(DR9, self).__init__(**kwargs)
        self.dasurl = 'http://data.sdss3.org/sas/dr10/boss/'

    def getDRNumber(self):
        return 10
        
    def _get_runlist_filename(self):
        return self._get_data_file('runList-dr10.par')

