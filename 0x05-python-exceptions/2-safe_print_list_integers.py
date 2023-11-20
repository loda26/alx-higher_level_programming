#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i, num = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            num++
        except (TypeError, ValueError):
            pass
        i++
    print()
    return num
