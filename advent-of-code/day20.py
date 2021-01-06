#!/usr/bin/env python3
import numpy as np
import pytest
import re

example = dict()
with open('example20.txt', 'r') as f:
    strings = f.read().splitlines()
    idx = None
    for item in strings:
        if ':' in item:
            if idx:
                example[idx] = tile
            idx = int(item.split(" ")[1].replace(":", ""))
            print(idx)
            tile = []
        elif item:
            tile.append([int(x) for x in item.replace(".", "0").replace("#", "1")])
            print(tile)
    example[idx] = tile # last tile

print(example)

input1 = dict()
with open('day20.txt', 'r') as f:
    strings = f.read().splitlines()
    idx = None
    for item in strings:
        if ':' in item:
            if idx:
                input1[idx] = tile
            idx = int(item.split(" ")[1].replace(":", ""))
            print(idx)
            tile = []
        elif item:
            tile.append([int(x) for x in item.replace(".", "0").replace("#", "1")])
            print(tile)
    input1[idx] = tile # last tile

print(input1)


def check_edge_match(edges_dict, edge):

    rev = np.flip(edge)

    match = -1 # will always match itself
    for tile in edges_dict:
        for e in edges_dict[tile]:
            if (edge == e).all() or (rev == e).all():
                match += 1
    
    return match

def part_one(input_dict):

    tiles = dict()
    for tile in input_dict:
        print(tile)
        tiles[tile] = np.array(input_dict[tile])

    # corner piece will have two un-matchable edges
    # edge piece will have one un-matchable edges
    # interior pieces must match all their edges
    edges = dict()
    for tile in tiles:
            edges_list = []
            top = tiles[tile][0, :]
            left = tiles[tile][:, 0]
            bottom = tiles[tile][-1, :]
            right = tiles[tile][:, -1]
            edges_list.append(top)
            edges_list.append(left)
            edges_list.append(bottom)
            edges_list.append(right)
            edges[tile] = edges_list

    product = 1
    for tile in edges:
        matches = 0
        for edge in edges[tile]:
            matches += check_edge_match(edges, edge)
        if matches == 2:
            print("tile {} is a corner piece".format(tile))
            product *= tile

    print("Part1: ", product)

def part_two(input_list):

    pass


if __name__ == "__main__":

    part_one(input1)
    # part_two(input_list)
