#!/usr/bin/python3
"""
Contains a function that implements utf-8 validation
"""


def validUTF8(data):
    """
    Validates if characters in data are UTF-8 and returns true if each
    integer is, else False
    """
    for i in data:
        bin_data = bin(i)
        if bin_data.startswith("-"):
            return False
        if len(bin_data) - 2 > 7:
            return False
    return True
