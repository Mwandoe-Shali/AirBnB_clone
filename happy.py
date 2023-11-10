#!/usr/bin/python3

def divisible_by_2(num):
    if num == 0:
        raise ZeroDivisionError
    for var in range(0, num):
        res = (num % 2)
        if res == 0 :
            return {f"{num} is divisible by 2."}
        else:
            return {f"{num} isn't divisible by 2."}
