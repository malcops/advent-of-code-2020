#!/usr/bin/env python3
import pytest
import re

input_list = []
with open('day16.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

rules = input_list[:input_list.index("your ticket:")]
nearby_tickets = input_list[input_list.index("nearby tickets:")+1:]
my_ticket = input_list[input_list.index("your ticket:")+1:input_list.index("nearby tickets:")]


def part_one(rules, tickets):

    range_strings = []
    for rule in rules:
        parts = rule.split(" ")
        RANGE_RE = r"[0-9]+-[0-9]+"
        for part in parts:
            if re.match(RANGE_RE, part):
                range_strings.append(part)

    valid_nums = []
    for r in range_strings:
        low_bound = int(r.split("-")[0])
        hi_bound = int(r.split("-")[1]) + 1
        valid_nums += list(range(low_bound, hi_bound))

    valid_nums = sorted(set(valid_nums))

    invalid_sum = 0
    valid_tickets = []
    for ticket in tickets:
        valid_ticket = True
        for val in ticket.split(","):
            if int(val) not in valid_nums:
                invalid_sum += int(val)
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    print("Part 1")
    print(invalid_sum)
    print(len(tickets))
    print(len(valid_tickets))
    return valid_tickets


@pytest.mark.parametrize("rules, tickets, my_ticket", [
                        (["class: 0-1 or 4-19",
                          "row: 0-5 or 8-19",
                          "seat: 0-13 or 16-19"], ["3,9,18", "15,1,5", "5,14,9"], ["11,12,13"]),
                         ])
def test_part_two(rules, tickets, my_ticket):

    mapping = part_two(rules, tickets, my_ticket)
    assert mapping['row'] == 0
    assert mapping['class'] == 1
    assert mapping['seat'] == 2


def part_two(rules, valid_tickets, my_ticket):

    rules_dict = dict()
    for rule in rules:
        field = rule.split(":")[0]
        valid_nums = []
        parts = rule.split(" ")
        RANGE_RE = r"[0-9]+-[0-9]+"
        for part in parts:
            if re.match(RANGE_RE, part):
                low_bound = int(part.split("-")[0])
                hi_bound  = int(part.split("-")[1]) + 1
                valid_nums += list(range(low_bound, hi_bound))
            rules_dict[field] = sorted(set(valid_nums))

    tickets = []
    for t in valid_tickets:
        tickets.append(t.split(","))

    print(len(tickets))
    print(tickets[0])
    mapping = {f: 0 for f in rules_dict}
    indexes = []
    for idx in range(len(tickets[0])):
        print(idx)
        print(tickets[0][idx])
        indexes.append([int(r[idx]) for r in tickets])

    print(rules_dict)
    print(tickets)
    print(indexes)

    assigned = []
    while len(assigned) < len(rules_dict):
        for field in rules_dict:
            valid = []
            for idx, nums in enumerate(indexes):
                all_there = all(item in rules_dict[field] for item in nums)
                if all_there and (idx not in assigned):
                    print(idx, nums)
                    print(rules_dict[field])
                    valid.append(idx)
                    print(valid)

            if len(valid) == 1:
                mapping[field] = valid[0]
                assigned.append(valid[0])

    print(mapping)
    print(len(rules_dict))
    print("assigned: ", assigned, len(assigned))

    # final calculation
    departure_idxs = [mapping[x] for x in mapping if x.startswith('departure')]
    print(departure_idxs)

    product = 1
    for idx in departure_idxs:
        product *= int(my_ticket[0].split(",")[idx])

    print("Part 2: ", product)
    return mapping


if __name__ == "__main__":

    valid_tickets = part_one(rules, nearby_tickets)
    print(my_ticket)
    part_two(rules, valid_tickets, my_ticket)
