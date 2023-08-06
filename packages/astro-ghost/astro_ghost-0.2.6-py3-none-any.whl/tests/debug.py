import os
import pytest
import sys
from astro_ghost.PS1QueryFunctions import *
from astro_ghost.TNSQueryFunctions import getTNSSpectra
from astro_ghost.NEDQueryFunctions import *
from astro_ghost.ghostHelperFunctions import *
from astro_ghost.stellarLocus import *
from astropy.coordinates import SkyCoord
from astropy import units as u
import pandas as pd
from datetime import datetime
import astro_ghost

#we want to include print statements so we know what the algorithm is doing
verbose = 1


#need to generate tests for stellarLocus, photoz_helper, DLR,
# PS1queryfunctions, and gradientAscent

def test_starSeparation():
    #classify a few galaxies, classify a few stars
    sourceType = ['galaxy',  'galaxy', 'star', 'star']
    ra = [186.7154417, 31.0672500, 191.0597417, 17.8279833]
    dec = [9.1342306, 20.8474806, 12.3629917, 33.2604472]
    sourceSet = []
    for i in np.arange(len(ra)):
        a = ps1cone(ra[i], dec[i], 1/3600)
        a = ascii.read(a)
        sourceSet.append(a.to_pandas().iloc[[0]])
    sourceDF = pd.concat(sourceSet, ignore_index=True)
    sourceDF['trueSourceClass'] = sourceType
    sourceDF = getColors(sourceDF)
    sourceDF = calc_7DCD(sourceDF)
    sourceDF = getNEDInfo(sourceDF)
    gals, stars = separateStars_STRM(sourceDF)
    #True is stars, False is gals. Passes if all gals are False and all stars are True!
    assert (np.nansum(gals['class'] == False) + np.nansum(stars['class'])) == len(sourceDF)


def test_plotLocus():
    #plot a subset of GHOST data compared to the tonry stellar locus
    GHOST = fullData()
    plotLocus(GHOST.iloc[0:500], color=False, save=True, type="Gals", timestamp="")
