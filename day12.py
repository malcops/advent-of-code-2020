#!/usr/bin/env python3
import pytest

input_list = []
with open('day12.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)


@pytest.mark.parametrize("direction, command, magnitude", [
                         ("F10", "F", 10),
                         ("N3", "N", 3), 
                         ("F7", "F", 7),
                         ("R90", "R", 90)
                         ])
def test_parse_direction(direction, command, magnitude):
    assert (command, magnitude) == parse_direction(direction)


def parse_direction(direction):
    command = direction[0]
    magnitude = int(direction[1:])
    return command, magnitude


@pytest.mark.parametrize("forward, command, magnitude, final", [
                         ("E", "R", 90, "S"),
                         ("E", "R", 180, "W"), 
                         ("E", "R", 270, "N"),
                         ("E", "R", 360, "E"),
                         ("E", "L", 90, "N"),
                         ("E", "L", 180, "W"), 
                         ("E", "L", 270, "S"),
                         ("E", "L", 360, "E")
                         ])
def test_calculate_rotation(forward, command, magnitude, final):
    
    assert calculate_rotation(forward, command, magnitude) == final


def calculate_rotation(forward, command, magnitude):
    directions = ("N", "E", "S", "W")
    idx = directions.index(forward)
    number = int(magnitude / 90)
    for x in range(number):
        if command == "R":
            idx += 1
        elif command == "L":
            idx -= 1
    if idx >= 0:
        idx = idx % len(directions)
    else:
        idx = idx
    return directions[idx]


def calculate_move(directions, command, magnitude):
    x = directions[command][0] * magnitude
    y = directions[command][1] * magnitude
    return (x,y)


def part_one(input_list):

    location = [0, 0]
    directions = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
    forward = {"F": "E"}
    rotations = ("R", "L")

    for direction in input_list:
        command, magnitude = parse_direction(direction)
        if command in directions:
            delta = calculate_move(directions, command, magnitude)
            location[0] = location[0] + delta[0]
            location[1] = location[1] + delta[1]
        if command in forward:
            delta = calculate_move(directions, forward["F"], magnitude)
            location[0] = location[0] + delta[0]
            location[1] = location[1] + delta[1]
        if command in rotations:
            forward["F"] = calculate_rotation(forward["F"], command, magnitude)
            # directions["F"] = delta

    print("Part 1")
    print(location)
    manhattan_distance = abs(location[0]) + abs(location[1])
    print(manhattan_distance)


@pytest.mark.parametrize("waypoint, command, magnitude, end", [
                         ([10, 4], "R", 90, [4, -10]),
                         ([10, 4], "R", 180, [-10, -4]),
                         ([10, 4], "R", 270, [-4, 10]),
                         ([10, 4], "R", 360, [10, 4]),
                         ([10, 4], "L", 90, [-4, 10]),
                         ([10, 4], "L", 180, [-10, -4]), 
                         ([10, 4], "L", 270, [4, -10]),
                         ([10, 4], "L", 360, [10, 4])
                         ])
def test_rotate_waypoint(waypoint, command, magnitude, end):

    assert end == rotate_waypoint(waypoint, command, magnitude)


def rotate_waypoint(waypoint, command, magnitude):
    number = int(magnitude / 90)
    for x in range(number):
        if command == "R":
            tmp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = -1 * tmp 
        if command == "L":
            tmp = waypoint[1]
            waypoint[1] = waypoint[0]
            waypoint[0] = -1 * tmp
    return waypoint

def part_two(input_list):

    directions = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
    rotations = ("R", "L")
    waypoint = [10, 1]
    location = [0, 0]

    for direction in input_list:
        command, magnitude = parse_direction(direction)
        if command == "F":
            location[0] = location[0] + (waypoint[0] * magnitude)
            location[1] = location[1] + (waypoint[1] * magnitude)
        if command in directions:
            delta = calculate_move(directions, command, magnitude)
            waypoint[0] = waypoint[0] + delta[0]
            waypoint[1] = waypoint[1] + delta[1]
        if command in rotations:
            waypoint = rotate_waypoint(waypoint, command, magnitude)

    print("Part 2")
    print(location)
    print(waypoint)
    manhattan_distance = abs(location[0]) + abs(location[1])
    print(manhattan_distance)


if __name__ == "__main__":

    part_one(input_list)
    # part_two(["F10", "N3", "F7", "R90", "F11"]) # Example
    part_two(input_list)
