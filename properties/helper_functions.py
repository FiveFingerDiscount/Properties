# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:57:34 2019
Helper functions for transforming scraped data to usefull format.
@author: LindenMa01
"""
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def no_build_year(x):
    # In some cases the build year is given in '-' if unknown
    if x is '-':
        x = None
    return x


def no_price_available(x):
    # Some prices are only available when asked
    if '.' not in x:
        x = None
    return x


def convert_to_int(x):
    # If a string consists only of numbers they are converted to an int
    if x.isdigit():
        x = int(x)
    return x
