# NICER utility script for barycentric correction and phaseogram generation
# This script reads event data after barycenteric correction, and returns the minimum BARYTIME

import sys

import numpy as np
from astropy.io import fits
from astropy.table import Table


def read_barytime(obsid):
    """
    Get the event data for a given observation ID.
    """
    event_filename = f"/Users/jacobpayne/Projects/Astronomyprojects/nicer_obs/{obsid}/xti/event_cl/ni{obsid}_0mpu7_cl_barycorr_PHASE.evt"
    hdu_list = fits.open(event_filename, memmap=True)
    evt_data = Table(hdu_list[1].data)
    min_barytime = np.min(evt_data["BARYTIME"])
    hdu_list.close()
    print(f"{min_barytime}")
    return min_barytime


read_barytime(sys.argv[1])
