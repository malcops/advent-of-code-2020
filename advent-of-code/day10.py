#!/usr/bin/env python3
import pytest

# adapter can take input 1,2,3 jolts lower than rating
# device is highest-rated adapter + 3
# outlet = 0
# don't skip any adapters

input_list = []
with open('day10.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(int(item))


def test_example():

    initial_list = [16,10,15,5,1,11,7,19,6,12,4]
    assert part_one(initial_list) == 35
    assert part_two(initial_list) == 8


def part_one(input_list):

    # add entry for outlet (0)
    ratings = input_list[:]
    ratings.append(0)
    ratings = sorted(ratings)

    # add entry for device's built in adapter (+3 the highest)
    ratings.append(ratings[-1] + 3)
    print(ratings)

    diff1 = 0
    diff2 = 0
    diff3 = 0
    for index, rating in enumerate(ratings):
        if index > 0:
            if (rating - ratings[index-1]) == 1:
                diff1 += 1
            elif (rating - ratings[index-1]) == 2:
                diff2 += 1
            elif (rating - ratings[index-1]) == 3:
                diff3 += 1
            else:
                assert 1 == 0

    print("Part 1: {}".format(diff1*diff3))
    print(diff1, diff2, diff3)
    return diff1*diff3


def part_two(input_list):

    ratings = input_list[:]
    ratings = sorted(ratings)

    # add entry for device's built in adapter (+3 the highest)
    ratings.append(ratings[-1] + 3)
    print(ratings)

    ways_to = {0: 1}
    for num in ratings:
        count = 0
        for x in range(1,4):
            if (num-x) in ways_to:
                count += ways_to[num-x]
        ways_to[num] = count

    print(ways_to[ratings[-1]])
    return ways_to[ratings[-1]]


if __name__ == "__main__":

    part_one(input_list)
    part_two(input_list)
