#!/usr/bin/env python3
import re

messages = []
rules = dict()
with open('day19.txt', 'r') as f:
    strings = f.read().splitlines()
    for item in strings:
        if item:
            if ": " in item:
                idx, info = item.split(": ")
                idx = int(idx)

                if '"' in info:
                    rule = info[1:-1]
                else:
                    rule = []
                    for i in info.split("|"):
                        rule.append(tuple(map(int, i.split())))
                rules[idx] = rule
            else:
                messages.append(item)


def build_regex(rules, rule_idx=0):

    rule = rules[rule_idx]
    if type(rule) is str:
        return rule

    options = []
    for option in rule:
        opt_str = ''
        for subrule in option:
            opt_str += build_regex(rules, subrule)
        options.append(opt_str)

    return '(' + '|'.join(options) + ')'


def build_regex_part_two(rules, rule_idx=0):

    rule = rules[rule_idx]
    if type(rule) is str:
        return rule

    # special rules
    if rule_idx == 8:
        # match rule 42 one or more times
        return '(' + build_regex_part_two(rules, 42) + ')+'
    if rule_idx == 11:
        # match rule 42 and 31 equal number of times
        r1 = build_regex_part_two(rules, 42)
        r2 = build_regex_part_two(rules, 31)
        options = []
        for n in range(1, 40):
            r_str = '{r1}{{{n}}}{r2}{{{n}}}'.format(r1=r1, n=n, r2=r2)
            options.append(r_str)
        return '(' + '|'.join(options) + ')'

    options = []
    for option in rule:
        opt_str = ''
        for subrule in option:
            opt_str += build_regex_part_two(rules, subrule)
        options.append(opt_str)

    return '(' + '|'.join(options) + ')'


def part_one(rules_dict, msg_list):

    regex = build_regex(rules_dict, 0)
    MESSAGE_RE = r"^{}$".format(regex)

    count = 0
    for msg in msg_list:
        if bool(re.match(MESSAGE_RE, msg)):
            count += 1

    print("Part1: ", count)


def part_two(rules_dict, msg_list):

    regex = build_regex_part_two(rules_dict, 0)
    MESSAGE_RE = r"^{}$".format(regex)

    count = 0
    for msg in msg_list:
        if bool(re.match(MESSAGE_RE, msg)):
            count += 1
    print("Part2: ", count)


if __name__ == "__main__":

    part_one(rules.copy(), messages)
    part_two(rules.copy(), messages)
