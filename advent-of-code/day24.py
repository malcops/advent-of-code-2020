#!/usr/bin/env python3
import pytest
import time

input_list = []
with open('day24.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

@pytest.mark.parametrize("input_string, output", [
                         ("esenee", ["e", "se", "ne", "e"]),
                         ])
def test_parse_line(input_string, output):

    assert parse_line(input_string) == output

def parse_line(string):
    instructions = []
    idx = 0
    max_idx = len(string)
    while idx < max_idx:
        if string[idx] in ("e", "w"):
            instructions.append(string[idx])
            idx += 1
        else:
            instructions.append(string[idx:idx+2])
            idx += 2
    return instructions

@pytest.mark.parametrize("instructions, delta", [
                         (["e", "e"], (2, 0)),
                         (["e", "w"], (0, 0)),
                         (["sw", "ne"], (0, 0)),
                         (["se", "nw"], (0, 0)),
                         (["nw", "w", "sw", "e", "e"], (0, 0))
                         ])
def test_execute_instructions(instructions, delta):
    assert delta == execute_instructions(instructions)


def execute_instructions(instructions):

    execution_dict = dict()
    execution_dict["e"] = (1, 0)
    execution_dict["w"] = (-1, 0)
    execution_dict["se"] = (1, -1)
    execution_dict["sw"] = (0, -1) # intentionally 0 in x
    execution_dict["ne"] = (0, 1) # intentionally 0 in x
    execution_dict["nw"] = (-1, 1)

    x_coord = 0
    y_coord = 0
    for ins in instructions:
        x, y = execution_dict[ins]
        x_coord += x
        y_coord += y

    return x_coord, y_coord


def part_one(input_list):

    black_tiles = []
    for ins in input_list:
        x, y = execute_instructions(parse_line(ins))
        if (x,y) in black_tiles:
            black_tiles.remove((x,y))
        else:
            black_tiles.append((x,y))

    print("Part 1: ", len(black_tiles))


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
