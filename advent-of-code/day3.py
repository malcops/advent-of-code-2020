#!/usr/bin/env python3
import pytest

input_map = []
with open('day3.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_map.append(item)

print(len(input_map))
print('\n'.join(input_map))

x_position = 0
y_position = 0
map_width = len(input_map[0])
map_length = len(input_map)
print(map_width)
print(map_length)

# PART 1
tree_count = 0
while(y_position < map_length):
    if input_map[y_position][x_position%map_width] == '#':
        print(x_position, y_position, x_position%map_width)
        print('tree')
        tree_count += 1
    x_position += 3
    y_position += 1
print('total trees: {}'.format(tree_count))


# PART 2
slopes = ( (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) )
tree_counts = []
for pair in slopes:
    x_slope = pair[0]
    y_slope = pair[1]

    tree_count = 0
    y_position = 0
    x_position = 0
    while(y_position < map_length):
        if input_map[y_position][x_position%map_width] == '#':
            tree_count += 1
        x_position += x_slope
        y_position += y_slope
    print("x_slope: {} y_slope: {}".format(x_slope, y_slope))
    print("total trees: {}".format(tree_count))
    tree_counts.append(tree_count)
    print(tree_counts)

prod = 1
for count in tree_counts:
    prod *= count

print("Final answer: {}".format(prod))
