#!/usr/bin/env python3
import pytest

# 7 chars for rows
# 128 rows - 0-127 
# F = lower half
# B = upper half

# 3 chars for columns
# 0-7
# L = lower half
# R = upper half

# seatID =  row * 8 + column

def find_column(code):

    assert len(code) == 3

    min = 0
    max = 8

    while (code):
        if code[0] == 'L':
            max = int(round((min+max)/2))
        else:
            min = int(round((min+max)/2))
        code = code[1:]

    return min


def find_row(code):

    assert len(code) == 7

    min = 0
    max = 128
    while (code):
        if code[0] == 'F':
            max = int(round((min+max)/2))
        else:
            min = int(round((min+max)/2))
        code = code[1:]

    return min


def process_boarding_pass(bp):

    assert len(bp) == 10
    row = find_row(bp[0:7])
    column = find_column(bp[7:10])
    seatID = row * 8 + column
    return (row, column, seatID)


@pytest.mark.parametrize("bp_code, column", [
                         ("LLL", 0),
                         ("RLL", 4),
                         ("RLR", 5),
                         ("RRR", 7)])
def test_find_column(bp_code, column):

    assert find_column(bp_code) == column


@pytest.mark.parametrize("bp_code, row", [
                         ("FBFBBFF", 44)])
def test_find_row(bp_code, row):

    assert find_row(bp_code) == row


@pytest.mark.parametrize("bp_code, output", [
                         ("BFFFBBFRRR", (70, 7, 567)),
                         ("FFFBBBFRRR", (14, 7, 119)),
                         ("BBFFBBFRLL", (102, 4, 820))])
def test_process_boarding_pass(bp_code, output):

    assert process_boarding_pass(bp_code) == output
    

input_list = []
with open('day5.txt', 'r') as f:

    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)
print(len(input_list))


# PART 1
highest_seatID = 0
for bp in input_list:
    _, _, seatID = process_boarding_pass(bp)
    if seatID > highest_seatID:
        highest_seatID = seatID
print(highest_seatID)


# PART 2
seatIDs = []
for bp in input_list:
    _, _, seatID = process_boarding_pass(bp)
    seatIDs.append(seatID)

sorted_seatIDs = list(sorted(seatIDs))
for seat in sorted_seatIDs:
    if (seat - 1) not in sorted_seatIDs:
        print(seat)
        print("missing seat before")
    if (seat + 1) not in sorted_seatIDs:
        print(seat)
        print("missing seat after")
