from pathlib import Path
import pandas as pd
import re

res = Path("./2024/res")


def parse_input():
    with open(res / "day_3.txt") as f:
        code = f.read()
    pt = r"mul\((\d+),(\d+)\)"
    return re.findall(pt, code)

def part1():
    muls = parse_input()
    print(sum([int(i[0]) * int(i[1]) for i in muls]))


part1()

#######################################################################
# Part 2

def parse_input():
    with open(res / "day_3.txt") as f:
        code = f.read()
    pt = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    return re.findall(pt, code)

def part2():
    matches = parse_input()
    # print(matches)
    total = 0
    flag = True
    for m in matches:
        if m == "do()":
            flag = True
        elif m == "don't()":
            flag = False
        elif flag:
            numbers = re.findall(r"\d+", m)
            total += int(numbers[0]) * int(numbers[1])
    print(total)

part2()