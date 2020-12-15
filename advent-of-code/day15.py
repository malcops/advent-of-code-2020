#!/usr/bin/env python3
import pytest
import time

example1 = [0, 3, 6]
example2 = [1, 3, 2]
example3 = [2, 1, 3]
example4 = [1, 2, 3]
example5 = [2, 3, 1]
example6 = [3, 2, 1]
example7 = [3, 1, 2]
input_list = [0, 8, 15, 2, 12, 1, 4]


@pytest.mark.parametrize("test_input, expected", [
                        (example1, 436),
                        (example2, 1),
                        (example3, 10),
                        (example4, 27),
                        (example5, 78),
                        (example6, 438),
                        (example7, 1836)
                         ])
def test_part_one(test_input, expected):

    assert part_one(test_input) == expected


def part_one(input_list):

    x = play_game(input_list, 2020)
    print("Part1: ", x)
    return x


@pytest.mark.parametrize("test_input, expected", [
                        (example1, 175594),
                        (example2, 2578),
                        (example3, 3544142),
                        (example4, 261214),
                        (example5, 6895259),
                        (example6, 18),
                        (example7, 362)
                         ])
def test_part_two(test_input, expected):

    assert part_two(test_input) == expected


def part_two(input_list):

    x = play_game(input_list, 30000000)
    print("Part2: ", x)
    return x


def play_game(input_list, max_index):

    max_index = max_index
    indexes = {x: "X" for x in range(0, max_index)}

    # last item will be processed below
    for idx, x in enumerate(input_list[:-1]):
        indexes[x] = idx + 1

    # e.g. if input_list has 3 items, we are starting turn 4
    turn = len(input_list) + 1
    last_added = input_list[-1]

    while turn <= max_index:
        if indexes[last_added] == "X":
            next_number = 0
        else:
            next_number = turn - 1 - indexes[last_added]
        indexes[last_added] = turn - 1
        last_added = next_number
        turn += 1

    return last_added


if __name__ == "__main__":

    start = time.time()
    part_one(input_list)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(input_list)
    stop = time.time()
    print("time: ", stop - start)
