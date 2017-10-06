'''
This module provides movie tools for level 0/1 SUVI  fits file
'''

from copy import deepcopy
from datetime import timedelta

import numpy as np
import numpy.ma as ma
import matplotlib.colors as colors
import matplotlib.animation
from pandas import DataFrame
from astropy.table import Table
from astropy.io import fits as pyfits
import astropy.units as u
from astropy.visualization.mpl_normalize import ImageNormalize
from astropy import visualization
from astropy.wcs import WCS
import sunpy.io
import sunpy.time
import sunpy.cm as cm
import sunpy.map
from sunpy.map import GenericMap
from sunpy.map.map_factory import Map


__all__ = ['SUVIMap']

from sunpy import config
TIME_FORMAT = config.get("general", "time_format")

# the following value is only appropriate for byte scaled images
BAD_PIXEL_VALUE = -200
# the following value is only appropriate for unscaled images
BAD_PIXEL_VALUE_UNSCALED = -32768


class SUVIMap(GenericMap):
    """
    A 2D IRIS Slit Jaw Imager Map.

    The Interface Region Imaging Spectrograph (IRIS) small explorer spacecraft
    provides simultaneous spectra and images of the photosphere, chromosphere,
    transition region, and corona with 0.33 to 0.4 arcsec spatial resolution,
    2-second temporal resolution and 1 km/s velocity resolution over a
    field-of- view of up to 175 arcsec by 175 arcsec.  IRIS consists of a 19-cm
    UV telescope that feeds a slit-based dual-bandpass imaging spectrograph.

    Slit-jaw images in four different passbands (C ii 1330, Si iv 1400,
    Mg ii k 2796 and Mg ii wing 2830  A) can be taken simultaneously with
    spectral rasters that sample regions up to 130 arcsec by 175 arcsec at a
    variety of spatial samplings (from 0.33 arcsec and up).
    IRIS is sensitive to emission from plasma at temperatures between
    5000 K and 10 MK.

    IRIS was launched into a Sun-synchronous orbit on 27 June 2013.

    References
    ----------
    * `IRIS Mission Page <http://iris.lmsal.com>`_
    * `IRIS Analysis Guide <https://iris.lmsal.com/itn26/itn26.pdf>`_
    * `IRIS Instrument Paper <https://www.lmsal.com/iris_science/doc?cmd=dcur&proj_num=IS0196&file_type=pdf>`_
    * `IRIS FITS Header keywords <https://www.lmsal.com/iris_science/doc?cmd=dcur&proj_num=IS0077&file_type=pdf>`_
    """

    def __init__(self, data, header, **kwargs):
        """Creates a new instance"""
        header.set('cdelt1', float(header.get('cdelt1')[0:3]))
        header.set('cdelt2', float(header.get('cdelt2')[0:3]))
        header.set('lonpole', int(header.get('lonpole')[0:3]))
        header.set('crota', float(header.get('crota')[0:3]))
        header.set('crota2', float(header.get('crota2')[0:3]))
        header.set('ctype2', 'HPLT-TAN')
        header.remove('hgln_obs')
        header.remove('hglt_obs')
        GenericMap.__init__(self, data, header, **kwargs)
        #if header.get('lvl_num') == 1:
        self.meta['wavelnth'] = header.get('wavelnth')
        self.meta['detector'] = header.get('instrid')
        self.meta['waveunit'] = header.get('waveunit')


        palette = cm.get_cmap('sdoaia' + str(int(self.meta['wavelnth'])))
        #palette.set_bad('black')
        #self.mask = np.ma.masked_less(fits[0].data, 0).mask
        self.plot_settings['cmap'] = palette
        self.plot_settings['norm'] = ImageNormalize(stretch=visualization.AsinhStretch(0.1))

    @classmethod
    def is_datasource_for(cls, data, header, **kwargs):
        """Determines if header corresponds to an SUVI image"""
        satid = header.get('SATID', '').startswith('GOES-')
        obs = header.get('INSTRID', '').startswith('SUVI_FM')
        #level = header.get('lvl_num') == 1
        return satid and obs


