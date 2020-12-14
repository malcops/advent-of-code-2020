#!/usr/bin/env python3
import itertools
import pytest
import re

input_list = []
with open('day14.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)


def parse_mask(mask_line):
    mask = mask_line.split(' ')[-1]
    return mask


def parse_memory(memory_line):

    ADDR_REGEX = r"\[([0-9_]+)\]"
    address = re.search(ADDR_REGEX, memory_line).group(0)[1:-1]
    value = memory_line.split('=')[-1]
    return address, value


@pytest.mark.parametrize("memory, value, mask, result", [
                        (0, 11,  'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 73),
                        (0, 101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101),
                        (0, 0,   'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 64)
                         ])
def test_apply_mask(memory, value, mask, result):

    assert apply_mask(memory, value, mask) == result


def apply_mask(memory, value, mask):

    and_str = ''
    for val in mask:
        if val == 'X':
            and_str += '1'
        else:
            and_str += '0'

    or_str = ''
    for val in mask:
        if val == '1':
            or_str += '1'
        else:
            or_str += '0'

    and_mask = int(and_str, 2)
    or_mask  = int(or_str, 2)

    # AND with bits we want to overwrite
    tmp = (int(value) & and_mask)
    # OR with mask
    result = (tmp | or_mask)

    return result


@pytest.mark.parametrize("value, mask, result", [
                        ('000000000000000000000000000000101010', '000000000000000000000000000000X1001X', '000000000000000000000000000000X1101X'),
                        ('000000000000000000000000000000011010', '00000000000000000000000000000000X0XX', '00000000000000000000000000000001X0XX'),
                         ])
def test_apply_mask_part2(value, mask, result):

    assert apply_mask_part2(value, mask) == result


def apply_mask_part2(address, mask):

    assert len(address) == len(mask)

    # bit = 0 -> memory address unchanged
    # bit = 1 -> memory address bit overwritten with 1
    # bit = X -> memory address bit is floating
    memory_str = ''

    for idx, bit in enumerate(mask):
        if mask[idx] == '0':
            memory_str += address[idx]
        elif mask[idx] == '1':
            memory_str += '1'
        else:
            memory_str += 'X'

    return memory_str


def update_memory(memory_str, memory, value):

    # indices
    addr_to_update = []
    memory_format = ''
    for idx, x in enumerate(memory_str):
        if x == "X":
            addr_to_update.append(idx)
            memory_format += "{}"
        else:
            memory_format += x

    # combos of indices e.g. [(0,0), (0,1), (1,0), (1,1)]
    combinations = list(itertools.product(range(2), repeat=len(addr_to_update)))
    addresses = []
    for combo in combinations:
        address = memory_format.format(*combo) # use tuple as format string!
        addresses.append(address)

    # update memory dict
    for addr in addresses:
        memory[addr] = int(value)

    return memory


def part_one(input_list):

    memory = dict()

    mask = ''
    for line in input_list:
        if 'mask =' in line:
            mask = parse_mask(line)
        elif 'mem' in line:
            address, value = parse_memory(line)
            memory[address] = apply_mask(memory.get(address, 0), value, mask)

    acc = 0
    for addr in memory:
        acc += memory[addr]
    print("part1")
    print(acc)


def part_two(input_list):

    memory = dict()
    mask = ''
    for line in input_list:
        if 'mask =' in line:
            mask = parse_mask(line)
        elif 'mem' in line:
            address, value = parse_memory(line)
            memory_str = apply_mask_part2(format(int(address), "036b"), mask)
            memory = update_memory(memory_str, memory, value)

    acc = 0
    for addr in memory:
        acc += memory[addr]
    print("part2")
    print(acc)


if __name__ == "__main__":

    part_one(input_list)
    part_two(input_list)
