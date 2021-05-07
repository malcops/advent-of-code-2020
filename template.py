#!/usr/bin/env python3
import pytest
import time

input_list = []
with open('day.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)



def part_one(input_list):

    pass


def part_two(input_list):

    pass


if __name__ == "__main__":

    start = time.time()
    part_one(input_list)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(input_list)
    stop = time.time()
    print("time: ", stop - start)
