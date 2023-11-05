#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    c_list = my_list.copy()
    c_list.sort()
    return c_list(-1)
