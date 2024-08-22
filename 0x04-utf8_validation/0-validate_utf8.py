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
        if i < 0 or i > 127:
            return False
    return True
