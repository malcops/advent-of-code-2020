#!/usr/bin/env python3
import pytest
import time

key1 = 18499292
key2 = 8790390


def transform(subject_number, loop_size):

    val = 1
    for _ in range(loop_size):
        val = val*subject_number
        val = val % 20201227

    return val


def reverse_transform(subject_number, key):

    val = 1
    loop_size = 0
    while val != key:
        val = val*subject_number
        val = val % 20201227
        loop_size += 1

    return loop_size


@pytest.mark.parametrize("subject_number, loop_size, output_key", [
                         (7, 11, 17807724),
                         (7, 8, 5764801),
                         (17807724, 8, 14897079)
                         ])
def test_transform(subject_number, loop_size, output_key):
    assert transform(subject_number, loop_size) == output_key


@pytest.mark.parametrize("subject_number, key, output_loop_size", [
                         (7, 17807724, 11),
                         (7, 5764801, 8),
                         (17807724, 14897079, 8)
                         ])
def test_reverse_transform(subject_number, key, output_loop_size):
    assert reverse_transform(subject_number, key) == output_loop_size


def part_one(key1, key2):

    print("keys: ", key1, key2)
    key1_loopsize = reverse_transform(7, key1)
    key2_loopsize = reverse_transform(7, key2)
    encryption_key = transform(key1, key2_loopsize)
    assert encryption_key == transform(key2, key1_loopsize)
    print("Part 1: ", encryption_key)


def part_two():

    pass


if __name__ == "__main__":

    start = time.time()
    part_one(key1, key2)
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two()
    stop = time.time()
    print("time: ", stop - start)
