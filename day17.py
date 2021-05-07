#!/usr/bin/env python3
import numpy as np
import pytest

example1 = [[0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]]

input1 = [[0, 0, 0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 1, 1, 0],
          [0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 1],
          [1, 1, 1, 1, 0, 0, 1, 1],
          [0, 0, 0, 1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 0, 0, 0]]


def process_cube(cube):

    assert len(cube.shape) == 3
    assert len(set(cube.shape)) == 1

    print(len(cube))
    start = 0
    stop = len(cube)
    new_cube = np.copy(cube)
    print(new_cube)
    for x in range(start, stop):
        for y in range(start, stop):
            for z in range(start, stop):
                if cube[x][y][z]:
                    print(x, y, z)
                    count = np.count_nonzero(cube[x-1:x+2, y-1:y+2, z-1:z+2])  # for the current cube
                    print(count-1)
                    if count-1 not in (2, 3):
                        print('turning off: ', x, y, z)
                        new_cube[x][y][z] = 0
                else:
                    count = np.count_nonzero(cube[x-1:x+2, y-1:y+2, z-1:z+2])
                    if count == 3:
                        print("turning on: ", x, y, z)
                        new_cube[x][y][z] = 1

    return new_cube


def process_4d(array):
    assert len(array.shape) == 4
    assert len(set(array.shape)) == 1
    start = 0
    stop = len(array)
    new_array = np.copy(array)
    print(new_array)
    for x in range(start, stop):
        for y in range(start, stop):
            for z in range(start, stop):
                for w in range(start, stop):
                    if array[x][y][z][w]:
                        print(x, y, z, w)
                        count = np.count_nonzero(array[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2])  # -1 for the current cube
                        print(count-1)
                        if count-1 not in (2, 3):
                            print('turning off: ', x, y, z, w)
                            new_array[x][y][z][w] = 0
                    else:
                        count = np.count_nonzero(array[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2])
                        if count == 3:
                            print("turning on: ", x, y, z, w)
                            new_array[x][y][z][w] = 1
    return new_array


@pytest.mark.parametrize("input_array, output_dimensions", [
                         (np.full((3, 3, 3), 1), (5, 5, 5)),
                         ])
def test_grow_by_one(input_array, output_dimensions):

    output = grow_by_one(input_array)
    assert output.shape == output_dimensions
    assert output[0][0][0] == 0
    assert output[4][4][4] == 0
    assert output[1][1][1] == 1


def grow_by_one(array):
    return np.pad(array, 1, mode='constant')


def part_one(input_list):
    a = np.array(input_list, ndmin=3)
    a_slice = np.full_like(a, fill_value=0)
    print(a.shape)
    print(a_slice.shape)
    array = np.concatenate([a_slice, a, a_slice], 0)
    print(array.shape)
    array = np.concatenate([a_slice, array, a_slice], 0)
    print(array.shape)
    array = np.concatenate([a_slice, array, a_slice], 0)
    print(array.shape)
    array = np.concatenate([array, a_slice], 0)
    print(array.shape)
    assert np.count_nonzero(array) == 24
    it = 0
    array = grow_by_one(array)
    array = process_cube(array)
    count = np.count_nonzero(array)
    print(count)
    assert np.count_nonzero(array) == 77
    it = 1
    array = grow_by_one(array)
    array = process_cube(array)
    count = np.count_nonzero(array)
    print(count)
    assert np.count_nonzero(array) == 66
    it = 2

    while it != 6:
        print("Iteration: ", it)
        array = grow_by_one(array)
        array = process_cube(array)
        it += 1
    count = np.count_nonzero(array)
    print(array.shape)
    print("Part1: ", count)
    return count


def part_two(input_list):
    # a = np.array(input_list, ndmin=4)
    # print(a.shape)
    # a_slice = np.full_like(a, fill_value=0)
    # array = np.concatenate([a_slice, a, a_slice], 0)
    # print(array.shape)
    # array = np.concatenate([a_slice, array, a_slice], 0)
    # print(array.shape)
    # array = np.concatenate([a_slice, array, a_slice], 0)
    # print(array.shape)
    # array = np.concatenate([array, a_slice], 0)
    # print(array.shape)
    # array = np.concatenate([a_slice, array, a_slice], 3)
    # print(array.shape)
    print(len(input_list))
    size_tuple = (len(input_list), len(input_list), len(input_list), len(input_list))
    print(size_tuple)
    array = np.zeros(size_tuple, dtype=int)
    input_array = np.array(input_list, ndmin=2)
    array[:][:][2][2] = input_array
    array = grow_by_one(array)
    array = grow_by_one(array)
    array = grow_by_one(array)
    it = 0
    print(array.shape)
    array = process_4d(array)
    count = np.count_nonzero(array)
    print(count)
    it = 1
    array = grow_by_one(array)
    array = process_4d(array)
    count = np.count_nonzero(array)
    print(count)
    it = 2
    while it != 6:
        print("Iteration: ", it)
        array = grow_by_one(array)
        array = process_4d(array)
        it += 1
    count = np.count_nonzero(array)
    print(array.shape)
    print("Part2: ", count)
    # 1432 - too high
    # 1392
    return count


if __name__ == "__main__":

    part_one(input1)
    part_two(input1)
