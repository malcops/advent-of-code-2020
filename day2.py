#!/usr/bin/env python3
import pytest


def is_line_valid(mini, maxi, char, pwd):
    if mini <= pwd.count(char) <= maxi:
        return True
    else:
        return False


@pytest.mark.parametrize("input_line, valid", [
                         ("1-3 a: abcde", True),
                         ("1-3 b: cdefg", False),
                         ("2-9 c: ccccccccc", True)])
def test_is_line_valid(input_line, valid):

    # * is for tuple expansion
    assert is_line_valid(*parse_line(input_line)) == valid


def parse_line(line):
    mini = 0
    maxi = 0
    char = ""
    pwd = ""

    mini = int(line.split("-", 1)[0])
    remainder = line.split("-", 1)[1]

    maxi = int(remainder.split(" ", 1)[0])
    remainder = str(remainder.split(" ", 1)[1])

    char = remainder.split(":", 1)[0]
    remainder = remainder.split(":", 1)[1]
    pwd = remainder.strip()

    return mini, maxi, char, pwd


@pytest.mark.parametrize("input_line, mini, maxi, char, pwd", [
                         ("1-3 a: abcde", 1, 3, "a", "abcde"),
                         ("1-3 b: cdefg", 1, 3, "b", "cdefg"),
                         ("2-9 c: ccccccccc", 2, 9, "c", "ccccccccc")])
def test_parse_line(input_line, mini, maxi, char, pwd):

    o_mini, o_maxi, o_char, o_pwd = parse_line(input_line)

    assert o_mini == mini
    assert o_maxi == maxi
    assert o_char == char
    assert o_pwd  == pwd


@pytest.mark.parametrize("input_line, valid", [
                         ("1-3 a: abcde", True),
                         ("1-3 b: cdefg", False),
                         ("2-9 c: ccccccccc", False)])
def test_is_line_valid_part2(input_line, valid):

    # * is for tuple expansion
    assert is_line_valid_part2(*parse_line(input_line)) == valid


def is_line_valid_part2(pos1, pos2, char, pwd):
    '''pos1 and pos2 are known as mini and maxi in Part 1'''

    # offset pos1 and pos2 by 1, to account for lack of zero-index
    pos1 = pos1 - 1
    pos2 = pos2 - 1

    # valid if only one position contains char
    # XOR => bool(a) != bool(b)
    if (pwd[pos1] == char) != (pwd[pos2] == char):
        return True
    else:
        return False


lines = []
with open('day2.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            lines.append(item)
print(len(lines))

# PART 1
count = 0
for line in lines:
    if is_line_valid(*parse_line(line)):
        count += 1
print(count)

# PART 2
count = 0
for line in lines:
    if is_line_valid_part2(*parse_line(line)):
        count += 1
print(count)
