#!/usr/bin/env python3
import pytest
import sys

# acc -> accumulator
# starts at 0

# jmp -> jump
# number is offset relative to itself

# nop -> no operation, go to instruction directly below

def parse_instruction(instruction):
    splits = instruction.split(" ")
    arg = splits[0]
    num = int(splits[1])
    return arg, num


def execute(instructions):
    pc = 0
    acc = 0
    finish_pc = len(instructions)
    executed_list = []
    while pc not in executed_list:
        arg, num = parse_instruction(instructions[pc])
        executed_list.append(pc)
        if arg == "acc":
            acc += num
            pc += 1
        elif arg == "nop":
            pc += 1
        elif arg == "jmp":
            pc += num

        if pc == finish_pc:
            print("Program executed successfully")
            print(pc, acc, "\n")
            return pc, acc

    print("Program exiting due to infinite loop\n")
    return pc, acc


input_list = []
with open('day8.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)


if __name__ == "__main__":

    # PART 1
    _, acc = execute(input_list)
    print("Part 1: {}".format(acc))

    # PART 2
    correct_pc = len(input_list)
    print("Correct PC: {}".format(correct_pc)) #651
    print(input_list[0])
    for index, ins in enumerate(input_list):

        instructions_copy = input_list[:] # force new copy!
        arg, num = parse_instruction(ins)
        if arg == "acc":
            print(f"skip index {index} with instruction {ins}\n")
        elif arg == "jmp":
            edited_instruction = "{} {}".format("nop", num)
            print(f"editing index {index}")
            print(f"{input_list[index]}")
            print(f"{edited_instruction}")
            instructions_copy[index] = edited_instruction
            print(input_list[0:10])
            print(instructions_copy[0:10])
            pc, acc = execute(instructions_copy)
        elif arg == "nop":
            edited_instruction = "{} {}".format("jmp", num)
            print(f"editing index {index}")
            print(f"{input_list[index]}")
            print(f"{edited_instruction}")
            instructions_copy[index] = edited_instruction
            print(input_list[0:10])
            print(instructions_copy[0:10])
            pc, acc = execute(instructions_copy)
