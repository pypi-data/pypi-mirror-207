import os
import pytest
import sys
from astro_ghost.PS1QueryFunctions import getAllPostageStamps
from astro_ghost.TNSQueryFunctions import getTNSSpectra
from astro_ghost.NEDQueryFunctions import *
from astro_ghost.ghostHelperFunctions import *
from astropy.coordinates import SkyCoord
from astropy import units as u
import pandas as pd
from datetime import datetime
import astro_ghost

#we want to include print statements so we know what the algorithm is doing
verbose = 1

def test_getGHOST():
    #Download the GHOST database.
    #note: real=False creates an empty database, which
    #allows you to use the association methods without
    #needing to download the full database first

    getGHOST(real=True, verbose=verbose, clobber=True)
    #test that it got the ghost database
    df = fullData()
    # GHOST has the correct match for at least NGC 2997
    assert df.loc[df['TransientName'] == 'SN2003jg', 'NED_name'].values[0] == 'NGC 2997'

def test_NED():
    # test our ability to snag a galaxy name from NED, using the coordinates of NGC 4321
    df = pd.DataFrame({'objID':23412341234, 'raMean':[185.7288750], 'decMean':[15.82230]})
    df = getNEDInfo(df)
    assert df['NED_name'].values[0] == 'NGC 4321'

def test_associate():
    #create a list of the supernova names, their skycoords, and their classes (these three are from TNS)
    snName = ['SN 2012dt', 'SN 1998bn', 'SN 1957B']

    snCoord = [SkyCoord(14.162*u.deg, -9.90253*u.deg, frame='icrs'), \
            SkyCoord(187.32867*u.deg, -23.16367*u.deg, frame='icrs'), \
            SkyCoord(186.26125*u.deg, +12.899444*u.deg, frame='icrs')]

    snClass = ['SN IIP', 'SN', 'SN Ia']

    # run the association algorithm with the DLR method!
    hosts = getTransientHosts(snName, snCoord, snClass, verbose=verbose, starcut='gentle', ascentMatch=False)
    
    correctHosts = [SkyCoord(14.1777425*u.deg, -9.9138756*u.deg, frame='icrs'), 
                    SkyCoord(187.3380517*u.deg, -23.1666716*u.deg, frame='icrs'), 
                    SkyCoord(186.2655971*u.deg, 12.8869831*u.deg, frame='icrs')]

    sep = []
    for i in np.arange(len(correctHosts)):
       c1 = correctHosts[i]
       c2 = SkyCoord(hosts['TransientRA'].values[i]*u.deg, hosts['TransientDEC'].values[i]*u.deg, frame='icrs')
       sep.append(c2.separation(c2).arcsec)

    #consider a success if the three hosts were found to a 1'' precision
    assert np.nanmax(sep) < 1
