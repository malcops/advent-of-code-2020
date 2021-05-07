#!/usr/bin/env python3
import pytest
import re

input_list = []
with open('day18.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            input_list.append(item)


def evaluate_expression_lr(expression):
    OPERATION_RE = r"[0-9]+ [+*] [0-9]+"

    while re.search(OPERATION_RE, expression):
        x = re.search(OPERATION_RE, expression)
        repl = str(eval(x.group(0)))
        expression = re.sub(OPERATION_RE, repl, expression, 1)
    return int(expression)


@pytest.mark.parametrize("expression, result", [
                         ("1 + 2 * 3 + 4 * 5 + 6", 71),
                         ("1 + (2 * 3) + (4 * (5 + 6))", 51),
                         ("2 * 3 + (4 * 5)", 26),
                         ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
                         ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
                         ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
                         ])
def test_evaluate_lr(expression, result):

    assert evaluate_lr(expression) == result


def evaluate_lr(expression):

    BRACKETS_RE = r"(\([0-9+* ]+\))"
    while re.search(BRACKETS_RE, expression):
        x = re.search(BRACKETS_RE, expression)
        brackets = x.group(0)
        inside_brackets = brackets[1:-1]
        repl = str(evaluate_expression_lr(inside_brackets))
        expression = re.sub(BRACKETS_RE, repl, expression, 1)

    return evaluate_expression_lr(expression)


@pytest.mark.parametrize("expression, result", [
                         ("1 + 2 * 3 + 4 * 5 + 6", 231),
                         ])
def test_evaluate_expression_addfirst(expression, result):

    assert evaluate_expression_addfirst(expression) == result


def evaluate_expression_addfirst(expression):
    ADD_RE = r"[0-9]+ [+] [0-9]+"

    while re.search(ADD_RE, expression):
        x = re.search(ADD_RE, expression)
        repl = str(eval(x.group(0)))
        expression = re.sub(ADD_RE, repl, expression, 1)

    # only multiplication remains
    return int(eval(expression))


@pytest.mark.parametrize("expression, result", [
                         ("1 + 2 * 3 + 4 * 5 + 6", 231),
                         ("1 + (2 * 3) + (4 * (5 + 6))", 51),
                         ("2 * 3 + (4 * 5)", 46),
                         ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
                         ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
                         ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340)
                         ])
def test_evaluate_addfirst(expression, result):

    assert evaluate_addfirst(expression) == result


def evaluate_addfirst(expression):

    BRACKETS_RE = r"(\([0-9+* ]+\))"
    while re.search(BRACKETS_RE, expression):
        x = re.search(BRACKETS_RE, expression)
        brackets = x.group(0)
        inside_brackets = brackets[1:-1]
        repl = str(evaluate_expression_addfirst(inside_brackets))
        expression = re.sub(BRACKETS_RE, repl, expression, 1)

    return evaluate_expression_addfirst(expression)


def part_one(input_list):

    count = 0
    for exp in input_list:
        count += evaluate_lr(exp)

    print("Part 1: ", count)


def part_two(input_list):

    count = 0
    for exp in input_list:
        count += evaluate_addfirst(exp)

    print("Part 2: ", count)


if __name__ == "__main__":

    part_one(input_list)
    part_two(input_list)
