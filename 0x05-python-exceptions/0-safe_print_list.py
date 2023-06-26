#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        s = 0
        for l in range(x):
            print("{}".format(my_list[s]), end="")
            s = s + 1
    except _:
        pass
    finally:
        print()
        return (s)
