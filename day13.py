#!/usr/bin/env python3
import pytest

input_list = []
with open('day13.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

def part_one(my_timestamp, bus_list):

    buses = [b for b in bus_list if b.isnumeric()]

    for x in range(my_timestamp, my_timestamp+100):
        for bus in buses:
            if (x % int(bus)) == 0:
                print("Part 1:")
                print(x, bus)
                print(int(bus) * (x - my_timestamp))
                return int(bus) * (x - my_timestamp)


@pytest.mark.parametrize("bus_list, timestamp", [
                         (['17', 'x', '13', '19'], 3417),
                         (['67', '7', '59', '61'], 754018),
                         (['67', 'x', '7', '59', '61'], 779210),
                         (['67', '7', 'x', '59', '61'], 1261476),
                         (['1789', '37', '47', '1889'], 1202161486)
                         ])
def test_part_two(bus_list, timestamp):

    assert part_two(bus_list) == timestamp


def part_two(bus_list):
    
    required_buses = []
    for idx, bus in enumerate(bus_list):
        if bus.isnumeric():
            required_buses.append(int(bus))
        else:
            required_buses.append(bus)

    step = required_buses[0]
    floor = 0
    T = 1
    for off, bus in enumerate(required_buses[1:]):
        if bus == 'x':
            pass
        else:
            solved = False
            idx = 1
            offset = off +1
            while not solved:
                T = floor + step * idx
                solved = (T + offset) % bus == 0
                print(T, bus, offset, idx, solved)
                idx += 1
            floor = T
            step = step * bus
    return T 


if __name__ == "__main__":

    my_timestamp = int(input_list[0])
    bus_list = []
    for x in input_list[1].split(','):
        bus_list.append(x)
    print(bus_list)

    part_one(my_timestamp, bus_list)
    part_two(bus_list)
