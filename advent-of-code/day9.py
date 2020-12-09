#!/usr/bin/env python3
import pytest

# 25 numbers - preamble
# after that, each number is the sum of 2 of the 25 previous numbers
# these 2 numbers are not equals
# there could be more than one pair

input_list = []
with open('day9.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(int(item))


def valid_next_element(queue, element):
    for item in queue:
        if (element - item) in queue:
            return True
    return False


def part_one(data_list, preamble):
    index = preamble
    q = data_list[0:preamble]
    while valid_next_element(q, data_list[index]):
        q.append(data_list[index])
        q.pop(0)
        index +=1
    print("Part 1: {}".format(data_list[index]))
    return data_list[index]


def part_two(data_list, part_one):

    for index, item in enumerate(data_list):
        subtotal = 0
        idx = index
        #print(f"trying {index}, {item}")
        while(subtotal < part_one):
            subtotal += data_list[idx]
            #print(f"added idx {idx}={data_list[idx]} to get {subtotal}")
            if subtotal == part_one:
               print("Part 2:")
               print(f"sum from index {index} to {idx}")
               print(data_list[index:idx+1])
               sorted_range = sorted(list(data_list[index:idx+1]))
               print(f"encryption weakness = {sorted_range[0] + sorted_range[-1]}")
               return
            idx += 1


if __name__ == "__main__":

    first_invalid = part_one(input_list, 25)

    part_two(input_list, first_invalid)
