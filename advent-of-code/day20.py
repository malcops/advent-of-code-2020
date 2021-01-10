#!/usr/bin/env python3
import numpy as np
import pytest
from scipy import signal

# example = dict()
# with open('example20.txt', 'r') as f:
#     strings = f.read().splitlines()
#     idx = None
#     for item in strings:
#         if ':' in item:
#             if idx:
#                 example[idx] = tile
#             idx = int(item.split(" ")[1].replace(":", ""))
#             print(idx)
#             tile = []
#         elif item:
#             tile.append([int(x) for x in item.replace(".", "0").replace("#", "1")])
#             print(tile)
#     example[idx] = tile # last tile
#
# print(example)

input1 = dict()
with open('day20.txt', 'r') as f:
    strings = f.read().splitlines()
    idx = None
    tile = []
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
    input1[idx] = tile  # last tile


def check_edge_match(edges_dict, edge):

    rev = np.flip(edge)

    match = -1  # will always match itself
    matching_tiles = []
    for tile in edges_dict:
        for e in edges_dict[tile]:
            if (edge == e).all() or (rev == e).all():
                matching_tiles.append(tile)
                match += 1
    return match, matching_tiles


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

    # product = 1
    # for tile in edges:
    #     matches = 0
    #     for edge in edges[tile]:
    #         m, _ = check_edge_match(edges, edge)
    #         matches += m
    #     if matches == 2:
    #         print("tile {} is a corner piece".format(tile))
    #         product *= tile
    #     elif matches == 3:
    #         print("tile {} is an edge piece".format(tile))
    #     elif matches == 4:
    #         print("tile {} is an interior piece".format(tile))
    # print("Part1: ", product)

    return edges


test_tile1 = np.zeros((3, 3), dtype=int)
test_tile1[2][0] = 1

test_tile2 = np.zeros((3, 3), dtype=int)
test_tile2[0][2] = 1


@pytest.mark.parametrize("tile1, tile2", [
                         (test_tile1, test_tile2),
                         ])
def test_tile_orientation(tile1, tile2):

    t2 = tile_orientation(tile1, tile2)
    assert t2 is not None


def tile_orientation(tile1, tile2):

    for _ in range(4):
        tile2 = np.rot90(tile2, 1)
        if (tile1[-1][:] == tile2[0][:]).all():
            return tile2

    tile2 = np.flip(tile2, 1)

    for _ in range(4):
        tile2 = np.rot90(tile2, 1)
        if (tile1[-1][:] == tile2[0][:]).all():
            return tile2

    return None


# global tiles
tiles = dict()
for tile in input1:
    tiles[tile] = np.array(input1[tile])

manual_topleft = tiles[3769].copy()
manual_topleft = np.rot90(manual_topleft, -1)
manual_topleft = np.flip(manual_topleft, axis=1)


@pytest.mark.parametrize("tile1, tile2, tile3", [
                         (manual_topleft, tiles[1823], tiles[2917]),
                         ])
def test_orient_lr(tile1, tile2, tile3):

    r1 = orient_lr(tile1, tile2)
    print(tile1)
    print(r1)

    r2 = orient_lr(r1, tile3)
    print(r1)
    print(r2)


def orient_lr(tile1, tile2):

    for _ in range(4):
        tile2 = np.rot90(tile2, 1)
        if (tile1[:, -1] == tile2[:, 0]).all():
            return tile2

    tile2 = np.flip(tile2, 1)

    for _ in range(4):
        tile2 = np.rot90(tile2, 1)
        if (tile1[:, -1] == tile2[:, 0]).all():
            return tile2

    assert 1 == 0

    return None


EXAMPLE_WATER = [[0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                 [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
                 [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                 [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                 [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                 [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
                 [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
                 [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                 [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
                 [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
                 [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1]]


def part_two(input_dict, edges):

    tiles = dict()
    for tile in input_dict:
        tiles[tile] = np.array(input_dict[tile])

    corners = []
    sides = []
    interior = []
    # copy from part 1
    for tile in edges:
        matches = 0
        for edge in edges[tile]:
            m, _ = check_edge_match(edges, edge)
            matches += m

        if matches == 2:
            print("tile {} is a corner piece".format(tile))
            corners.append(tile)
        elif matches == 3:
            print("tile {} is an edge piece".format(tile))
            sides.append(tile)
        elif matches == 4:
            print("tile {} is an interior piece".format(tile))
            interior.append(tile)

    matches = []
    t = 1663
    for edge in edges[t]:
        _, m = check_edge_match(edges, edge)
        matches += m
    print(set(matches))
    for m in set(matches):
        if m in sides:
            print("{} is a side piece".format(m))
        if m in interior:
            print("{} is an interior piece".format(m))

    # t= corner piece -> gives edges column
    t = 3769
    col = [t]
    next_col = []
    for idx in range(12):
        matches = []
        for edge in edges[t]:
            _, m = check_edge_match(edges, edge)
            matches += m
        new = [x for x in set(matches) if x is not t]
        new = [x for x in new if x not in col]
        if idx == 0:
            col.append(new[0])  # change this between 0,1 to get x/y vector
            next_col.append(new[1])
            t = new[0]
        else:
            for n in new:
                if n in sides:
                    col.append(n)
                    t = n
                if n in interior:
                    next_col.append(n)
                elif n in corners:
                    print("done column: ", n)
    print(col)
    print(next_col)

# 0,0  >>>>> y0 row
#  v
#  v
#  v
# x0
# col

# determine semi-programatically
    x0 = [3769, 3089, 1553, 1663, 2647, 2539, 3181, 1163, 2297, 1171, 2777, 1019]
    x1 = [1823, 2749, 3299, 1997, 1049, 3037, 1579, 3821, 3041, 2473, 2851, 2423]
    x2 = [2917, 1223, 1567, 1381, 3797, 2143, 1723, 2879, 1657, 2333, 1291, 2593]
    x3 = [3361, 1447, 1811, 1867, 3989, 3637, 1901, 3109, 1973, 1543, 1307, 2029]
    x4 = [2309, 2663, 2477, 2557, 2083, 1289, 3659, 1789, 1283, 3541, 2957, 2887]
    x5 = [1327, 1733, 3079, 3697, 3671, 3643, 3257, 1847, 1483, 1753, 3527, 1511]
    x6 = [3359, 1583, 1493, 2087, 2693, 1693, 2713, 3083, 1487, 2069, 2657, 1559]
    x7 = [1409, 2399, 2927, 2441, 2801, 1621, 2741, 3169, 3163, 2003, 3301, 1427]
    x8 = [2797, 2683, 2803, 3407, 2617, 3767, 1597, 1949, 3761, 3049, 1367, 3907]
    x9 = [2999, 1987, 3331, 3673, 1009, 1889, 2549, 3517, 1181, 2699, 3061, 1913]
    x10 = [3923, 1861, 2017, 1783, 1499, 1213, 1039, 3121, 3119, 2843, 2551, 1061]
    x11 = [1097, 3691, 2389, 3613, 1741, 3677, 1933, 2179, 3469, 2347, 3739, 3557]

    y0 = [3769, 1823, 2917, 3361, 2309, 1327, 3359, 1409, 2797, 2999, 3923, 1097]
    y1 = [3089, 2749, 1223, 1447, 2663, 1733, 1583, 2399, 2683, 1987, 1861, 3691]
    y2 = [1553, 3299, 1567, 1811, 2477, 3079, 1493, 2927, 2803, 3331, 2017, 2389]
    y3 = [1663, 1997, 1381, 1867, 2557, 3697, 2087, 2441, 3407, 3673, 1783, 3613]
    y4 = [2647, 1049, 3797, 3989, 2083, 3671, 2693, 2801, 2617, 1009, 1499, 1741]
    y5 = [2539, 3037, 2143, 3637, 1289, 3643, 1693, 1621, 3767, 1889, 1213, 3677]
    y6 = [3181, 1579, 1723, 1901, 3659, 3257, 2713, 2741, 1597, 2549, 1039, 1933]
    y7 = [1163, 3821, 2879, 3109, 1789, 1847, 3083, 3169, 1949, 3517, 3121, 2179]
    y8 = [2297, 3041, 1657, 1973, 1283, 1483, 1487, 3163, 3761, 1181, 3119, 3469]
    y9 = [1171, 2473, 2333, 1543, 3541, 1753, 2069, 2003, 3049, 2699, 2843, 2347]
    y10 = [2777, 2851, 1291, 1307, 2957, 3527, 2657, 3301, 1367, 3061, 2551, 3739]
    y11 = [1019, 2423, 2593, 2029, 2887, 1511, 1559, 1427, 3907, 1913, 1061, 3557]

    # used to determine rows and columns above

    # print("working")
    # prev = x9
    # cur = x10
    # idx = 11
    # t = y0[idx]
    # this = []
    # this.append(t)
    # for x in cur[1:-1]:
    #     matches = []
    #     for edge in edges[x]:
    #         _, m = check_edge_match(edges, edge)
    #         matches += m
    #     new = [t for t in matches if t not in prev]
    #     new = [t for t in new if t not in cur]
    #     new = [t for t in new if t not in sides]
    #     this.append(new[0])
    # this.append(y11[idx])

    rows = (y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11)
    cols = (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)

    solved = np.array([y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11])
    print(solved)

    # manually determined to be a corner piece w/ correct orientation
    top_left = 3769
    top_left = np.rot90(tiles[top_left], -1)
    top_left = np.flip(top_left, axis=1)

    correct_tiles = dict()
    correct_tiles[3769] = top_left.copy()
    tile_above = top_left

    # this is only x0 vector
    for t in x0[1:]:
        print(t)
        correct = tile_orientation(tile_above, tiles[t])
        assert correct is not None
        correct_tiles[t] = correct
        tile_above = correct
    print(correct_tiles)

    # rest of columns
    for idx, y in enumerate(y0):
        if idx == 0:
            pass
        else:
            top_tile = y
            left_of_top_tile = y0[idx-1]
            corrected_top_tile = orient_lr(correct_tiles[left_of_top_tile], tiles[top_tile])
            correct_tiles[top_tile] = corrected_top_tile
            tile_above = corrected_top_tile
            for t in cols[idx][1:]:
                print(t)
                correct = tile_orientation(tile_above, tiles[t])
                correct_tiles[t] = correct
                tile_above = correct

    # print(correct_tiles[2551], 2551)
    # print(correct_tiles[1061], 1061)
    # print(correct_tiles[3739], 3739)
    print(correct_tiles[3557], 3557)

    # write total_grid and CSV
    tile_size = 10
    grid_size = 12
    total_grid = np.zeros((tile_size*grid_size, tile_size*grid_size))

    xmin = 0
    xmax = 10
    ymin = 0
    ymax = 10
    for x in cols:
        for y in x:
            total_grid[ymin:ymax, xmin:xmax] = correct_tiles[y]
            ymin += 10
            ymax += 10
        xmin += 10
        xmax += 10
        ymin = 0
        ymax = 10

    np.savetxt('pm.csv', total_grid, fmt='%d', delimiter=',')

    # TODO - remove tile "edges"
    water = np.zeros((8*grid_size, 8*grid_size), dtype=int)
    assert water.shape == (96, 96)
    xmin = 0
    xmax = 8
    ymin = 0
    ymax = 8
    for x in cols:
        for y in x0:
            print(y)
            water[ymin:ymax, xmin:xmax] = correct_tiles[y][1:-1, 1:-1]
            ymin += 8
            ymax += 8
        xmin += 8
        xmax += 8
        ymin = 0
        ymax = 8

    np.savetxt('output1.txt', water, fmt='%d')

    edges = (0, 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 99, 100, 109, 110, 119, 120, 129, 130,)

    # final_grid = np.delete(total_grid[0][:], total_grid)
    np.savetxt('day20-output.txt', total_grid, fmt='%d')

    print(total_grid.shape)
    final_grid = np.zeros((96, 120), dtype=int)
    final_grid_idx = 0
    for idx, y in enumerate(total_grid):
        if idx not in edges:
            print(idx, y)
            final_grid[final_grid_idx][:] = y
            final_grid_idx += 1

    np.savetxt('intermediate.txt', final_grid, fmt='%d')

    water = np.zeros((96, 96), dtype=int)
    water_idx = 0
    for idx, x[:] in enumerate(final_grid.T):
        if idx not in edges:
            water[water_idx][:] = x
            water_idx += 1

    np.savetxt('output2.txt', water.T, fmt='%d')
    assert water.shape == (96, 96)

    seamonster_text = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
    seamonster_text = [line.replace('#', '1').replace(' ', '0') for line in seamonster_text]
    seamonster_kernel = np.array([[int(char) for char in line] for line in seamonster_text])

    assert (seamonster_kernel == SEA_MONSTER).all()

    monsters = find_monsters(water, SEA_MONSTER)
    monster_size = np.count_nonzero(np.array(SEA_MONSTER))
    print(monsters, monster_size)
    roughness = np.count_nonzero(water) - monsters*monster_size
    print("Part2 :", roughness)


SEA_MONSTER = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
               [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

monster1 = [[1, 0, 1]]
water1 = [[0, 0, 1, 1, 1, 0, 0, 1, 0, 1]]

monster2 = [[1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]]
water2 = [[0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 1]]


def monster_there(water, seamonster_kernel):
    result_space = signal.convolve2d(water, seamonster_kernel, mode='valid')
    result_space = result_space.astype(np.uint8)
    return np.count_nonzero(result_space == seamonster_kernel.sum())


@pytest.mark.parametrize("water, monster, num", [
                         (EXAMPLE_WATER, SEA_MONSTER, 2),
                         (np.pad(SEA_MONSTER, 10, mode='constant'), SEA_MONSTER, 1),
                         (water2, monster2, 1),
                         (water1, monster1, 2)
                         ])
def test_find_sea_monster(water, monster, num):

    if type(water) == list:
        water = np.array(water)
    if type(monster) == list:
        monster = np.array(monster)
    assert num == find_monsters(water, monster)


def find_monsters(water, monster):

    size = np.count_nonzero(monster)
    count = 0
    print("size", size)

    for _ in range(4):
        water = np.rot90(water, 1)
        finds = signal.convolve2d(water, monster)
        print(water)
        print(np.amax(finds))
        count = np.count_nonzero(finds == size)
        if count:
            return count

    water = np.flip(water, 1)
    print(water)

    for _ in range(4):
        water = np.rot90(water, 1)
        finds = signal.convolve2d(water, monster)
        print(np.amax(finds))
        count = np.count_nonzero(finds == size)
        if count:
            return count

    return count


if __name__ == "__main__":

    edges = part_one(input1)
    part_two(input1, edges)
