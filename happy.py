#!/usr/bin/python3
# Checks if a number is divisible by 2

def divisible_by_2(num):
    #A func implenetation.
    if num == 0:
        raise ZeroDivisionError
    for var in range(0, num):
        res = (num % 2)
        if res == 0 :
            print (f"{num} is divisible by 2.")

        else:
            print (f"{num} isn't divisible by 2.")
        num -= 1

nambari = int(input("What number do you want to test: "))
divisible_by_2(nambari)