#!/usr/bin/env python3
import numpy as np
import pytest
import time

input_list = []
with open('day24.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

example = []
with open('day24-example.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            example.append(item)


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
                         (["nw", "w", "sw", "e", "e"], (0, 0)),
                         (["e", "sw", "e", "e"], (3, 1)),
                         (["e", "e", "e", "sw", "sw"], (3, 2))
                         ])
def test_execute_instructions(instructions, delta):
    assert delta == execute_instructions(instructions)


def print_grid(array):
    for idx, row in enumerate(array):
        offset = len(array)-idx
        string = " "*offset + str(row)
        print(string)


ex = np.zeros((4, 4), dtype=int)
print_grid(ex)


def execute_instructions(instructions):

    execution_dict = dict()
    execution_dict["e"] = (1, 0)
    execution_dict["w"] = (-1, 0)
    execution_dict["se"] = (1, 1)
    execution_dict["sw"] = (0, 1)  # intentionally 0 in x
    execution_dict["ne"] = (0, -1)  # intentionally 0 in x
    execution_dict["nw"] = (-1, -1)

    x_coord = 0
    y_coord = 0
    for ins in instructions:
        x, y = execution_dict[ins]
        x_coord += x
        y_coord += y

    return x_coord, y_coord


def test_part_one():
    count, _ = part_one(example)
    assert count == 10

    count, _ = part_one(input_list)
    assert count == 269


def part_one(input_list):

    black_tiles = []
    for ins in input_list:
        x, y = execute_instructions(parse_line(ins))
        if (x, y) in black_tiles:
            black_tiles.remove((x, y))
        else:
            black_tiles.append((x, y))

    print("Part 1: ", len(black_tiles))
    print(black_tiles)
    return len(black_tiles), black_tiles


def process_array(array):
    new_array = np.copy(array)
    start = 0
    stop = len(array) - 1
    # for y in array:
    #     for x in array:
    #         print(count_neighbors(array, x, y))
    for y in range(start, stop):
        for x in range(start, stop):
            count = count_neighbors(array, x, y)
            if (array[y][x] == 0) and (count == 2):
                new_array[y][x] = 1
            if (array[y][x] == 1) and (count not in (1, 2)):
                new_array[y][x] = 0
        # for x in y:
            # print(count_neighbors(array, x, y))
    return new_array


def count_neighbors(array, x, y):

    count = array[y-1][x-1] + array[y-1][x] + array[y][x+1] + array[y+1][x+1] + array[y+1][x] + array[y][x-1]
    return count


def part_two(black_tiles_list):

    array = np.zeros((30, 30), dtype=int)
    print(array.shape)

    # shift everything left and up (positive only)
    x_min = 0
    y_min = 0
    for tile in black_tiles_list:
        if tile[0] < x_min:
            x_min = tile[0]
        if tile[1] < y_min:
            y_min = tile[1]
    print(x_min, y_min)
    x_shift = abs(x_min)
    y_shift = abs(y_min)

    for tile in black_tiles_list:
        x_adj = tile[0] + x_shift
        y_adj = tile[1] + y_shift
        array[y_adj][x_adj] = 1
        if tile == (0, 0):
            array[y_adj][x_adj] = 1

    array = np.pad(array, 1, mode='constant')
    array = np.pad(array, 1, mode='constant')
    print_grid(array)

    for day in range(1, 101):
        array = process_array(array)
        array = np.pad(array, 1, mode='constant')
        print("Day {}: {}".format(day, np.count_nonzero(array)))


if __name__ == "__main__":

    start = time.time()
    _, black_tiles = part_one(input_list)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(black_tiles)
    stop = time.time()
    print("time: ", stop - start)
