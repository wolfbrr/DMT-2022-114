"""
This module provides a number of some help ml tools.
"""
from datetime import datetime
def my_convert_to_number(x, default=None):
    """ converts input to a number or None if input is not a number """
    try:
        return float(x)
    except:
        return default

def my_convert_to_date(x, default=None):
    """ converts input to a datetime object """
    if isinstance(x, datetime):
        return x
    else:
        try:
            return datetime.strptime(x, "%d-%m-%Y")
        except:
            try:
                return datetime.strptime(x, "%d/%m/%Y")
            except:
                try:
                    return datetime.strptime(x, "%d.%m.%Y")
                except:
                    try:
                        return datetime.strptime(x, "%d-%m-%y")
                    except:
                        try:
                            return datetime.strptime(x, "%d/%m/%y")
                        except:
                            try:
                                return datetime.strptime(x, "%d.%m.%y")
                            except:
                                try:
                                    return datetime.strptime(x, "%d-%m-%Y %H:%M:%S")
                                except:
                                    return default
