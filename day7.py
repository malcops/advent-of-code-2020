#!/usr/bin/env python3
import pytest

@pytest.mark.parametrize("rule, bag_type, contains", [
                         ("light red bags contain 1 bright white bag, 2 muted yellow bags.", "light red", ["bright white", "muted yellow"]),
                         ("dark orange bags contain 3 bright white bags, 4 muted yellow bags.", "dark orange", ["bright white", "muted yellow"])])
def test_parse_rule(rule, bag_type, contains):

    bag, contents = parse_rule(rule)
    assert bag == bag_type
    assert contents == contains


def parse_rule(rule):
    words = rule.split(" ")
    bag_type = " ".join(words[0:2])
    contains = []
    remaining = words[3:]
    for index, word in enumerate(remaining):
        if 'bag' in word:
            bag_to_add = " ".join(remaining[index-2:index])
            if bag_to_add != "no other":
                contains.append(bag_to_add)

    return bag_type, contains


@pytest.mark.parametrize("rule, bag_type, contains", [
                         ("light red bags contain 1 bright white bag, 2 muted yellow bags.", "light red", {"bright white":1, "muted yellow":2}),
                         ("dark orange bags contain 3 bright white bags, 4 muted yellow bags.", "dark orange", {"bright white": 3, "muted yellow": 4})])
def test_parse_numbers(rule, bag_type, contains):

    bag, contents = parse_numbers(rule)
    assert contents == contains


def parse_numbers(rule):
    words = rule.split(" ")
    bag_type = " ".join(words[0:2])
    contains = dict()
    remaining = words[3:]
    for index, word in enumerate(remaining):
        if 'bag' in word:
            bag_to_add = " ".join(remaining[index-2:index])
            if bag_to_add != "no other":
                number = int(remaining[index-3])
                contains[bag_to_add] = number
    return bag_type, contains


def process_bag(bag, bag_rules):

    if bag_rules[bag] == []:
        return False
    elif 'shiny gold' in bag_rules[bag]:
        return True
    else:
        ret = False
        for b in bag_rules[bag]:
            if process_bag(b, bag_rules):
                ret = True
    return ret


@pytest.mark.parametrize("bag, contains", [
                         ('wavy crimson', True),
                         ('drab green', True),
                         ('faded olive', True), # contains drab green
                         ('shiny gold', False),
                         ('bright gray', False)])
def test_process_bag(bag, contains):

    assert process_bag(bag, bag_rules) == contains


def count_other_bags(bag, bag_contents):
    count = 1
    print(bag_contents[bag])
    for b in bag_contents[bag]:
        count += count_other_bags(b, bag_contents) * bag_contents[bag][b]

    # subtract the original count = 1
    return count - 1


input_list = []
with open('day7.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

bag_rules = dict()
for rule in input_list:
    bag, contents = parse_rule(rule)
    bag_rules[bag] = contents
print(len(bag_rules))


if __name__ == "__main__":

    count = 0
    for bag in bag_rules:
        if process_bag(bag, bag_rules):
            count += 1
    print("Part1: {}".format(count))

    bag_contents = dict()
    for rule in input_list:
        bag, contents = parse_numbers(rule)
        bag_contents[bag] = contents

    print(count_other_bags('shiny gold', bag_contents))
