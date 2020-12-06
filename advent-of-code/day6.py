#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize("group, total", [
                         (["abc"], 3),
                         (["a", "b", "c"], 3),
                         (["ab", "ac"], 3),
                         (["a", "a", "a", "a"], 1)])
def test_calculate_group_total(group, total):

    assert calculate_group_total(group) == total


def calculate_group_total(group):
    
    group_string = ""
    for person in group:
        group_string += person
    
    group_total = len(set(group_string))
    return group_total


def calculate_group_total_part2(group):

    group_set = set("abcdefghijklmnopqrstuvwxyz")
    for person in group:
        person_set = set(person)
        group_set = group_set & person_set 
    
    return len(group_set)


input_list = []
with open('day6.txt', 'r') as f:
    strings = f.read().splitlines()
    group = []
    for item in strings:
        if item:
            group.append(item)
        else:
            if group:
                input_list.append(group)
            group = []

running_total = 0
for group in input_list:
    running_total += calculate_group_total(group)

print("Part 1: {}".format(running_total))

running_total = 0
for group in input_list:
    running_total += calculate_group_total_part2(group)

print("Part 2: {}".format(running_total))
