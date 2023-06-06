#!/usr/bin/python3
for first_digits in range(0, 10):
    for second_digits in range(first_digits + 1, 10):
        if first_digits == 8 and second_digits == 9:
            print("{}{}".format(first_digits, second_digits))
        else:
            print("{}{}".format(first_digits, second_digits), end=", ")
