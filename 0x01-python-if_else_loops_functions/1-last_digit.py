#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
digits = abs(num) % 10
if num < 0:
    digits = -digits
print("Last digit of {} is {} and is ".format(num, digits), end="")
if digits > 5:
    print("greater than 5")
elif digits == 0:
    print("0")
else:
    print("less than 6 and not 0")
