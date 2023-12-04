#!/usr/bin/python3
"""Module for lookup function"""

def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
