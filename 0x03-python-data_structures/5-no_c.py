#!/usr/bin/python3
def no_c(my_string):
    copy = [d for d in my_string if d != 'c' and d != 'C']
    return ("".join(copy))
