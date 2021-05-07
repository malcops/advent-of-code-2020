#!/usr/bin/env python3
import pytest
import re


def is_passport_valid(passport):
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    nonrequired_keys = ("cid")

    for key in required_keys:
        if key not in passport:
            return False
    return True


@pytest.mark.parametrize("passport, valid", [
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", True),
                         ("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929", False),
                         ("hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm", True),
                         ("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in", False)])
def test_is_passport_valid(passport, valid):

    assert is_passport_valid(passport) == valid


def is_passport_valid_part2(passport):

    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    nonrequired_keys = ("cid")

    # parse into key/value pairs
    passport_dict = dict(item.split(":") for item in passport.strip().split(" "))

    for key in required_keys:
        if key not in passport_dict:
            return False

    if not (1920 <= int(passport_dict.get("byr")) <= 2002):
        return False
    if not (2010 <= int(passport_dict.get("iyr")) <= 2020):
        return False
    if not (2020 <= int(passport_dict.get("eyr")) <= 2030):
        return False
    if "cm" in passport_dict.get("hgt"):
        if not (150 <= int(passport_dict.get("hgt")[:-2]) <= 193):
            return False
    elif "in" in passport_dict.get("hgt"):
        if not (59 <= int(passport_dict.get("hgt")[:-2]) <= 76):
            return False
    else:
        return False

    HCL_RE = R"^#[0-9a-f]{6}$"
    if not re.search(HCL_RE, passport_dict.get("hcl")):
        return False

    eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if passport_dict.get("ecl") not in eye_colors:
        return False

    PID_RE = R"^[0-9]{9}$"
    if not re.search(PID_RE, passport_dict.get("pid")):
        return False

    return True


@pytest.mark.parametrize("passport, valid", [
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:183cm ", True),
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2003 iyr:2017 cid:147 hgt:183cm ", False), # byr
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2021 cid:147 hgt:183cm ", False), # iyr
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:60in  ", True),
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:190cm ", True),
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:190in ", False), # hgt
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:190   ", False), # hgt
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#123abc byr:2002 iyr:2017 cid:147 hgt:183cm ", True),
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#123abz byr:2002 iyr:2017 cid:147 hgt:183cm ", False), # hcl
                         ("ecl:gry pid:860033327 eyr:2020 hcl:123abc byr:2002 iyr:2017 cid:147 hgt:183cm ", False), # hcl
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:183cm ", True),
                         ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:183cm ", True),
                         ("ecl:wat pid:860033327 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:183cm ", False), # ecl
                         ("ecl:gry pid:000000001 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:183cm ", True),
                         ("ecl:gry pid:0123456789 eyr:2020 hcl:#fffffd byr:2002 iyr:2017 cid:147 hgt:183cm ", False), # pid
                         ("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in", False)])
def test_is_passport_valid_part2(passport, valid):

    assert is_passport_valid_part2(passport) == valid


# PART 1
input_list = []
with open('day4.txt', 'r') as f:

    strings = f.read().splitlines()
    passport = ""
    for item in strings:
        if item:
            passport += " " + item
        else:
            if passport:
                input_list.append(passport)
            passport = ""

print(input_list)

valid = 0
for passport in input_list:
    if is_passport_valid(passport):
        valid += 1

print("PART1")
print("valid: {}".format(valid))

valid = 0
for passport in input_list:
    if is_passport_valid_part2(passport):
        valid += 1

print("PART2")
print("valid: {}".format(valid))
