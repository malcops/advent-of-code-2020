#!/usr/bin/env python3
import pytest
import time

round1_p1 = [9, 2, 6, 3, 1]
round1_p2 = [5, 8, 4, 7, 10]

round2_p1 = [2, 6, 3, 1, 9, 5]
round2_p2 = [8, 4, 7, 10]

round3_p1 = [6, 3, 1, 9, 5]
round3_p2 = [4, 7, 10, 8, 2]

round4_p1 = [3, 1, 9, 5, 6, 4]
round4_p2 = [7, 10, 8, 2]

round5_p1 = [1, 9, 5, 6, 4]
round5_p2 = [10, 8, 2, 7, 3]

# recursive combat
round6_p1 = [9, 5, 6, 4]
round6_p2 = [8, 2, 7, 3, 10, 1]

round7_p1 = [5, 6, 4, 9, 8]
round7_p2 = [2, 7, 3, 10, 1]

round8_p1 = [6, 4, 9, 8, 5, 2]
round8_p2 = [7, 3, 10, 1]

round9_p1 = [4, 9, 8, 5, 2]
round9_p2 = [3, 10, 1, 7, 6]

# infinite game rule

inf_p1 = [43, 19]
inf_p2 = [2, 29, 14]


input_list = []
with open('day22.txt',  'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)

p2_start = input_list.index("Player 2:")
deck1 = [int(x) for x in input_list[1:p2_start]]
deck2 = [int(x) for x in input_list[p2_start+1:]]


@pytest.mark.parametrize("deck1, deck2, deck1_after, deck2_after, winner", [
                        (round1_p1, round1_p2, round2_p1, round2_p2, 1),
                        (round2_p1, round2_p2, round3_p1, round3_p2, 2),
                        (round3_p1, round3_p2, round4_p1, round4_p2, 1),
                        (round4_p1, round4_p2, round5_p1, round5_p2, 2),
                        (round5_p1, round5_p2, round6_p1, round6_p2, 2),
                        (round6_p1, round6_p2, round7_p1, round7_p2, 1),
                         ])
def test_play_round(deck1, deck2, deck1_after, deck2_after, winner):

    d1, d2, w = play_round(deck1, deck2)
    assert d1 == deck1_after
    assert d2 == deck2_after
    assert w == winner


def play_round(deck1, deck2):

    winner = 0
    if deck1[0] > deck2[0]:
        winner = 1
        deck1.append(deck1.pop(0))
        deck1.append(deck2.pop(0))
    else:
        winner = 2
        deck2.append(deck2.pop(0))
        deck2.append(deck1.pop(0))

    return deck1, deck2, winner


def play_recursive_combat(deck1, deck2):

    winner = 0
    prev_hands = set()
    round = 1

    while deck1 and deck2:
        hand = tuple(deck1), tuple(deck2)
        if hand in prev_hands:
            print("Deck1 wins by default")
            print(calculate_score(deck1))
            return deck1, deck2, 1

        prev_hands.add(hand)

        d1 = deck1.pop(0)
        d2 = deck2.pop(0)
        if len(deck1) >= d1 and len(deck2) >= d2:
            _, _, winner = play_recursive_combat(deck1[:d1], deck2[:d2])
            print(winner)
        else:
            if d1 > d2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            deck1.append(d1)
            deck1.append(d2)
        elif winner == 2:
            deck2.append(d2)
            deck2.append(d1)
        else:
            print('wtf')
        round += 1

    if deck1:
        winner = 1
        print("Deck1 wins")
        print(round)
        print(deck1, deck2)
        print(calculate_score(deck1))
    else:
        winner = 2
        print("Deck2 wins")
        print(round)
        print(deck1, deck2)
        print(calculate_score(deck2))

    return deck1, deck2, winner


def calculate_score(deck):

    sum = 0
    for it, x in enumerate(reversed(deck), 1):
        sum += it * x

    return sum


def part_one(deck1, deck2):

    play_game(deck1, deck2)


def play_game(deck1, deck2):

    while deck1 and deck2:
        deck1, deck2, _ = play_round(deck1, deck2)

    if deck1:
        print("Deck1 wins")
        print(calculate_score(deck1))
    else:
        print("Deck2 wins")
        print(calculate_score(deck2))

    return deck1, deck2


def part_two(deck1, deck2):

    d1, d2, w = play_recursive_combat(deck1, deck2)
    print(calculate_score(d1))
    print(calculate_score(d2))


if __name__ == "__main__":

    start = time.time()
    part_one(deck1.copy(), deck2.copy())
    stop = time.time()
    print("time: ", stop - start)

    start = time.time()
    part_two(deck1.copy(), deck2.copy())
    stop = time.time()
    print("time: ", stop - start)
