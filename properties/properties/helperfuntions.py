# -*- coding: utf-8 -*-
# Helper functions for transforming scraped data to usefull format


def no_build_year(x):
    # In some cases the build year is given in '-' if unknown
    if x is '-':
        x = None
        return x


def empty_to_Null(self, x):
    if x is "":
        x = "Null"


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
