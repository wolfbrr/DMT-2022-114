"""
This module provides a number of some help ml tools.
"""

def my_convert_to_number(x, default=None):
    """ converts input to a number or None if input is not a number """
    try:
        return float(x)
    except:
        return default

