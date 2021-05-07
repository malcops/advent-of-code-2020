#!/usr/bin/env python3

numbers = []
with open('day1.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            numbers.append(int(item))

# PART 1
for x in numbers:
    for y in numbers:
        if (x + y == 2020):
            print(f"x, y = {x}, {y}")
            print(f"x * y = {x * y}")

# PART 2
for x in numbers:
    for y in numbers:
        for z in numbers:
            if (x + y + z == 2020):
                print(f"x, y, z = {x}, {y}, {z}")
                print(f"product = {x*y*z}")
