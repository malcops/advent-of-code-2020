#!/usr/bin/env python3
import time

example = [3, 8, 9, 1, 2, 5, 4, 6, 7]


def calculate_string(final_list):
    index1 = final_list.index(1)
    calc_list = final_list[index1+1:] + final_list[0:index1]
    calc_list = [str(x) for x in calc_list]
    return "".join(calc_list)


assert calculate_string([5, 8, 3, 7, 4, 1, 9, 2, 6]) == '92658374'


def pm_process(cups, cc):

    highest_cup = len(cups)
    c1 = cups[cc]
    c2 = cups[c1]
    c3 = cups[c2]

    found = False
    dest = cc
    while not found:
        dest = dest - 1
        if dest == 0:
            dest = highest_cup
        if dest not in (c1, c2, c3):
            found = True

    # set cc's 'next' to cup after the 3 removed
    cups[cc] = cups[c3]
    # grab dest cups current 'next' -> tmp
    tmp = cups[dest]
    # set dest cups 'next' to c1
    cups[dest] = c1
    # set c3's 'next' to tmp
    cups[c3] = tmp
    # return cc as current cups next
    return cups, cups[cc]


def pm(input_list, moves):

    c = input_list[:]
    cups = dict()
    for idx, cup in enumerate(c[:-1]):
        cups[cup] = c[idx+1]
    cups[c[-1]] = c[0]
    cc = c[0]
    # cups is dict of cups and the next cup in line
    for x in range(1, moves+1):
        print("-- move {} -- ".format(x))
        cups, cc = pm_process(cups, cc)

    idx = 1
    c1 = cups[idx]
    c2 = cups[c1]

    print(c1, c2)
    return c1 * c2


if __name__ == "__main__":

    my_input = [1, 5, 8, 9, 3, 7, 4, 6, 2]

    start = time.time()
    ans = pm(my_input, 100)
    stop = time.time()
    print("Part 1:", ans)
    print("time: ", stop-start)

    example_part2 = example[:] + list(range(10, 1000001))
    my_input_part2 = my_input[:] + list(range(10, 1000001))
    start = time.time()
    ans = pm(my_input_part2, 10000000)
    stop = time.time()
    print("Part 2:", ans)
    print("time: ", stop-start)
