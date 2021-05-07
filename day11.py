#!/usr/bin/env python3
import pytest

input_list = []
input_2darray = []
with open('day11.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)
            input_2darray.append([x for x in item])

example = []
example_2darray = []
with open('example_day11.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            example.append(item)
            example_2darray.append([x for x in item])


# EXAMPLES

example_it0 = ["L.LL.LL.LL",
               "LLLLLLL.LL",
               "L.L.L..L..",
               "LLLL.LL.LL",
               "L.LL.LL.LL",
               "L.LLLLL.LL",
               "..L.L.....",
               "LLLLLLLLLL",
               "L.LLLLLL.L",
               "L.LLLLL.LL"]

example_it1 = ["#.##.##.##",
               "#######.##",
               "#.#.#..#..",
               "####.##.##",
               "#.##.##.##",
               "#.#####.##",
               "..#.#.....",
               "##########",
               "#.######.#",
               "#.#####.##"]

example_it2 = ["#.LL.L#.##",
               "#LLLLLL.L#",
               "L.L.L..L..",
               "#LLL.LL.L#",
               "#.LL.LL.LL",
               "#.LLLL#.##",
               "..L.L.....",
               "#LLLLLLLL#",
               "#.LLLLLL.L",
               "#.#LLLL.##"]

example_it3 = ["#.##.L#.##",
               "#L###LL.L#",
               "L.#.#..#..",
               "#L##.##.L#",
               "#.##.LL.LL",
               "#.###L#.##",
               "..#.#.....",
               "#L######L#",
               "#.LL###L.L",
               "#.#L###.##"]

example_it4 = ["#.#L.L#.##",
               "#LLL#LL.L#",
               "L.L.L..#..",
               "#LLL.##.L#",
               "#.LL.LL.LL",
               "#.LL#L#.##",
               "..L.L.....",
               "#L#LLLL#L#",
               "#.LLLLLL.L",
               "#.#L#L#.##"]

example_it5 = ["#.#L.L#.##",
               "#LLL#LL.L#",
               "L.#.L..#..",
               "#L##.##.L#",
               "#.#L.LL.LL",
               "#.#L#L#.##",
               "..L.L.....",
               "#L#L##L#L#",
               "#.LLLLLL.L",
               "#.#L#L#.##"]

example_final = ["#.#L.L#.##",
                 "#LLL#LL.L#",
                 "L.#.L..#..",
                 "#L##.##.L#",
                 "#.#L.LL.LL",
                 "#.#L#L#.##",
                 "..L.L.....",
                 "#L#L##L#L#",
                 "#.LLLLLL.L",
                 "#.#L#L#.##"]


def print_grid(grid):
    print("\n".join(grid))
    print("\n")


@pytest.mark.parametrize("subgrid, new_seat", [
                         (["LLL", "L.L", "LLL"], "."),
                         (["LLL", "LLL", "L.L"], "#"),
                         (["#LL", "L#L", "##L"], "#"),   # 3
                         (["#L#", "L#L", "##L"], "L"),   # 4
                         (["###", "L#L", "##L"], "L"),   # 5
                         ])
def test_process_seat(subgrid, new_seat):
    print(subgrid)
    print_grid(subgrid)
    assert process_seat(subgrid) == new_seat


def pad_with_floor(grid):

    new_grid = []
    new_grid.insert(0, "." * (len(grid[0]) + 2))

    for row in grid:
        new_row = "." + row + "."
        new_grid.append(new_row)

    new_grid.append("." * (len(grid[0]) + 2))

    assert (len(grid) + 2) == len(new_grid)
    assert (len(grid[0]) + 2) == len(new_grid[1])

    return new_grid


def pad_2d_with_floor(array):
    new_array = []
    new_array.insert(0, list("." * (len(array[0]) + 2)))
    for row in array:
        new_row = row[:]
        new_row.append(".")
        new_row.insert(0, ".")
        new_array.append(new_row)
    new_array.append(list("." * (len(array[0]) + 2)))
    return new_array


def process_seat(subgrid):
    """3x3 grid

    if seat is empty, and no occupied seats adjacent, it becomes occupied
    if a seat is occupied, and 4 or more seats adjacent are occupied, the seat becomes empty
    otherwise, no change
    """
    assert len(subgrid) == 3
    assert len(subgrid[0]) == 3
    assert len(subgrid[1]) == 3
    assert len(subgrid[2]) == 3
    seat = subgrid[1][1]
    adjacent_seats = subgrid[0] + subgrid[1][0] + subgrid[1][2] + subgrid[2]
    if seat == ".":
        return "."
    elif seat == "L":
        if "#" not in adjacent_seats:
            return "#"
    elif seat == "#":
        if adjacent_seats.count("#") >= 4:
            return "L"

    return seat


part2_example = [
[".","#","#",".","#","#","."], # basic example w/ none found
["#",".","#",".","#",".","#"],
["#","#",".",".",".","#","#"],
[".",".",".","L",".",".","."],
["#","#",".",".",".","#","#"],
["#",".","#",".","#",".","#"],
[".","#","#",".","#","#","."]]

part2_example2 = [
[".",".",".",".",".",".",".",".",".",".",".",".","."],
[".","L",".","L",".","#",".","#",".","#",".","#","."], # only "sees" one
[".",".",".",".",".",".",".",".",".",".",".",".","."]]

part2_example_diag1 = [["#",".","#"],
                       [".","L","."],
                       ["#",".","#"]]

part2_example_diag2 = [["#",".","#"],
                       [".","#","."],
                       ["#",".","#"]] # 4 -> stays filled

part2_example_diag3 = [["#",".","#"],
                       [".","#","."],
                       ["#","#","#"]] # 5 -> goes to empty


def process_seat_part2(i, j, grid):
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    seat = grid[i][j]
    # print("seat: {}".format(seat))
    if seat == ".":
        return ".", 0
    else:
        count = 0
        idx = j-1
        while idx >= 0:                # LEFT
            if grid[i][idx] == "#":
                count += 1
                break
            elif grid[i][idx] == "L":
                break
            idx = idx - 1

        idx = j+1
        while idx <= max_x:            # RIGHT
            if grid[i][idx] == "#":
                count += 1
                break
            elif grid[i][idx] == "L":
                break
            idx = idx + 1

        idx = i-1
        while idx >= 0:                # UP
            if grid[idx][j] == "#":
                count += 1
                break
            elif grid[idx][j] == "L":
                break
            idx = idx - 1

        idx = i+1
        while idx <= max_y:            # DOWN
            if grid[idx][j] == "#":
                count += 1
                break
            elif grid[idx][j] == "L":
                break
            idx += 1

        idx = j-1
        idy = i-1
        while idx >= 0 and idy >= 0: # UP-LEFT
            if grid[idy][idx] == "#":
                count += 1
                break
            elif grid[idy][idx] == "L":
                break
            idx = idx-1
            idy = idy-1

        idx = j+1
        idy = i-1
        while idx <= max_x and idy >= 0: # UP-RIGHT
            if grid[idy][idx] == "#":
                count += 1
                break
            elif grid[idy][idx] == "L":
                break
            idx = idx+1
            idy = idy-1

        idx = j-1
        idy = i+1
        while idx >= 0 and idy <= max_y: # DOWN-LEFT
            if grid[idy][idx] == "#":
                count += 1
                break
            elif grid[idy][idx] == "L":
                break
            idx = idx-1
            idy = idy+1

        idx = j+1
        idy = i+1
        while idx <= max_x and idy <= max_y: # DOWN-RIGHT
            if grid[idy][idx] == "#":
                count += 1
                break
            elif grid[idy][idx] == "L":
                break
            idx = idx+1
            idy = idy+1

    if seat == "L" and count == 0:
        return "#", count
    elif seat == "#" and count >= 5:
        return "L", count
    else:
        return seat, count


part2_it0 = [
["L",".","L","L",".","L","L",".","L","L"],
["L","L","L","L","L","L","L",".","L","L"],
["L",".","L",".","L",".",".","L",".","."],
["L","L","L","L",".","L","L",".","L","L"],
["L",".","L","L",".","L","L",".","L","L"],
["L",".","L","L","L","L","L",".","L","L"],
[".",".","L",".","L",".",".",".",".","."],
["L","L","L","L","L","L","L","L","L","L"],
["L",".","L","L","L","L","L","L",".","L"],
["L",".","L","L","L","L","L",".","L","L"],
]

part2_it1 = [
["#",".","#","#",".","#","#",".","#","#"],
["#","#","#","#","#","#","#",".","#","#"],
["#",".","#",".","#",".",".","#",".","."],
["#","#","#","#",".","#","#",".","#","#"],
["#",".","#","#",".","#","#",".","#","#"],
["#",".","#","#","#","#","#",".","#","#"],
[".",".","#",".","#",".",".",".",".","."],
["#","#","#","#","#","#","#","#","#","#"],
["#",".","#","#","#","#","#","#",".","#"],
["#",".","#","#","#","#","#",".","#","#"],
]

part2_it2 = [
["#",".","L","L",".","L","L",".","L","#"],
["#","L","L","L","L","L","L",".","L","L"],
["L",".","L",".","L",".",".","L",".","."],
["L","L","L","L",".","L","L",".","L","L"],
["L",".","L","L",".","L","L",".","L","L"],
["L",".","L","L","L","L","L",".","L","L"],
[".",".","L",".","L",".",".",".",".","."],
["L","L","L","L","L","L","L","L","L","#"],
["#",".","L","L","L","L","L","L",".","L"],
["#",".","L","L","L","L","L",".","L","#"],
]

part2_it3 = [
["#",".","L","#",".","#","#",".","L","#"],
["#","L","#","#","#","#","#",".","L","L"],
["L",".","#",".","#",".",".","#",".","."],
["#","#","L","#",".","#","#",".","#","#"],
["#",".","#","#",".","#","L",".","#","#"],
["#",".","#","#","#","#","#",".","#","L"],
[".",".","#",".","#",".",".",".",".","."],
["L","L","L","#","#","#","#","L","L","#"],
["#",".","L","#","#","#","#","#",".","L"],
["#",".","L","#","#","#","#",".","L","#"],
]

part2_it4 = [
["#",".","L","#",".","L","#",".","L","#"],
["#","L","L","L","L","L","L",".","L","L"],
["L",".","L",".","L",".",".","#",".","."],
["#","#","L","L",".","L","L",".","L","#"],
["L",".","L","L",".","L","L",".","L","#"],
["#",".","L","L","L","L","L",".","L","L"],
[".",".","L",".","L",".",".",".",".","."],
["L","L","L","L","L","L","L","L","L","#"],
["#",".","L","L","L","L","L","#",".","L"],
["#",".","L","#","L","L","#",".","L","#"],
]

part2_it5 = [
["#",".","L","#",".","L","#",".","L","#"],
["#","L","L","L","L","L","L",".","L","L"],
["L",".","L",".","L",".",".","#",".","."],
["#","#","L","#",".","#","L",".","L","#"],
["L",".","L","#",".","#","L",".","L","#"],
["#",".","L","#","#","#","#",".","L","L"],
[".",".","#",".","#",".",".",".",".","."],
["L","L","L","#","#","#","L","L","L","#"],
["#",".","L","L","L","L","L","#",".","L"],
["#",".","L","#","L","L","#",".","L","#"],
]

part2_it6 = [
["#",".","L","#",".","L","#",".","L","#"],
["#","L","L","L","L","L","L",".","L","L"],
["L",".","L",".","L",".",".","#",".","."],
["#","#","L","#",".","#","L",".","L","#"],
["L",".","L","#",".","L","L",".","L","#"],
["#",".","L","L","L","L","#",".","L","L"],
[".",".","#",".","L",".",".",".",".","."],
["L","L","L","#","#","#","L","L","L","#"],
["#",".","L","L","L","L","L","#",".","L"],
["#",".","L","#","L","L","#",".","L","#"],
]

@pytest.mark.parametrize("i, j, grid, exp_seat, exp_count", [
                         (0, 0, example_2darray, "#", 0),
                         (3, 3, part2_example, "#", 0),
                         (1, 1, part2_example2, "#", 0),
                         (1, 3, part2_example2, "L", 1),
                         (1, 1, part2_example_diag1, "L", 4),
                         (1, 1, part2_example_diag2, "#", 4),
                         (1, 1, part2_example_diag3, "L", 5),
                         (1, 2, pad_2d_with_floor(part2_it0), ".", 0),
                         (1, 5, pad_2d_with_floor(part2_it0), ".", 0),
                         (2, 6, pad_2d_with_floor(part2_it0), "#", 0)
                         ])
def test_process_seat_part2(i, j, grid, exp_seat, exp_count):

    returned, returned_count = process_seat_part2(i, j, grid)
    assert returned == exp_seat
    assert returned_count == exp_count


def process_grid_part2(current_grid):
    input_grid = current_grid[:]
    # current_grid is padded, iterate only on the seats
    rows = len(input_grid) - 2
    seats = len(input_grid[0]) - 2
    single_row = list("."*len(input_grid[0]))
    updated_grid = []
    for x in range(0, len(input_grid)):
        updated_grid.append(single_row)
    # updated_grid = [("."*(len(input_grid[0])))] * (len(input_grid))

    for row in range(1, rows+1):
        new_row = ["."]
        for seat in range(1, seats+1):
            # same as part1 except need to pass whole grid
            new_seat, _ = process_seat_part2(row, seat, input_grid)
            new_row.append(new_seat)

        new_row.append(".")
        updated_grid[row] = new_row

    return input_grid, updated_grid


def process_grid(current_grid):

    print_grid(current_grid)
    input_grid = current_grid[:]
    print_grid(input_grid)
    # current_grid is padded, iterate only on the seats
    rows = len(input_grid) - 2
    seats = len(input_grid[0]) - 2
    updated_grid = [("."*(len(input_grid[0])))] * (len(input_grid))
    for row in range(1, rows+1):
        new_row = ""
        for seat in range(1, seats+1):
            new_row += process_seat([input_grid[row-1][seat-1:seat+2],
                                     input_grid[row][seat-1:seat+2],
                                     input_grid[row+1][seat-1:seat+2]])
        updated_grid[row] =  "." + new_row + "."

    print_grid(updated_grid)
    return input_grid, updated_grid


@pytest.mark.parametrize("input_grid, output_grid", [
                         (pad_with_floor(example_it0), pad_with_floor(example_it1)),
                         (pad_with_floor(example_it1), pad_with_floor(example_it2)),
                         (pad_with_floor(example_it2), pad_with_floor(example_it3)),
                         (pad_with_floor(example_it4), pad_with_floor(example_it5)),
                         (pad_with_floor(example_it5), pad_with_floor(example_final)),
                         ])
def test_process_grid(input_grid, output_grid):
    _, updated = process_grid(input_grid)
    for idx, row in enumerate(updated):
        assert row == output_grid[idx]


def test_part_one():

    count, grid = part_one(example)
    assert count == 37
    assert grid == pad_with_floor(example_final)


def part_one(input_grid):

    # pad grid with floor so it's possible to calculate edge seats!
    current_grid = pad_with_floor(input_grid[:])
    current, updated = process_grid(current_grid)

    iterations = 1
    while current != updated:
        iterations += 1
        current, updated = process_grid(updated)

    final_grid = updated
    all_seats = "".join(final_grid)
    print("Part 1:")
    print(iterations)
    print(all_seats.count("#"))
    return all_seats.count("#"), final_grid


def part_two(input_grid):

    current_grid = pad_2d_with_floor(input_grid[:])
    current, updated = process_grid_part2(current_grid)

    iterations = 1
    while current != updated:
        iterations += 1
        current, updated = process_grid_part2(updated)

    final_grid = updated
    for row in updated:
        print(row)
    print("Part 2:")
    print(iterations)
    count = 0
    for row in final_grid:
        for seat in row:
            if seat == "#":
                count += 1
    print(count)
    return count, final_grid


@pytest.mark.parametrize("input_grid, output_grid", [
                         (["#"], ["...", ".#.", "..."]),
                         (example_it0, ["............",
                                        ".L.LL.LL.LL.",
                                        ".LLLLLLL.LL.",
                                        ".L.L.L..L...",
                                        ".LLLL.LL.LL.",
                                        ".L.LL.LL.LL.",
                                        ".L.LLLLL.LL.",
                                        "...L.L......",
                                        ".LLLLLLLLLL.",
                                        ".L.LLLLLL.L.",
                                        ".L.LLLLL.LL.",
                                        "............"]),
                         ])
def test_pad_with_floor(input_grid, output_grid):

    output = pad_with_floor(input_grid)
    for idx, row in enumerate(output_grid):
        assert row == output[idx]


@pytest.mark.parametrize("input_grid, output_grid", [
                         (pad_2d_with_floor(part2_it0), pad_2d_with_floor(part2_it1)),
                         (pad_2d_with_floor(part2_it1), pad_2d_with_floor(part2_it2)),
                         (pad_2d_with_floor(part2_it2), pad_2d_with_floor(part2_it3)),
                         (pad_2d_with_floor(part2_it3), pad_2d_with_floor(part2_it4)),
                         (pad_2d_with_floor(part2_it4), pad_2d_with_floor(part2_it5)),
                         (pad_2d_with_floor(part2_it5), pad_2d_with_floor(part2_it6)),
                         ])
def test_process_grid_part2(input_grid, output_grid):

    print("\n")
    for row in input_grid:
        print(row)
    print("\n")
    x, updated = process_grid_part2(input_grid)

    assert x == input_grid

    for idx, row in enumerate(updated):
        assert row == output_grid[idx]


if __name__ == "__main__":

    part_one(input_list)
    part_two(input_2darray)