from pathlib import Path
import pandas as pd

res = Path("./2024/res")


def parse_input():
    reports = pd.read_csv(res / "day_2.txt", header=None, sep=" ", names=[0, 1, 2, 3, 4, 5, 6, 7])
    return reports

def check_inc(levels: pd.Series):
    for i in range(len(levels) - 1):
        l1, l2 = levels.iloc[i], levels.iloc[i + 1]
        if (l1 >= l2 or abs(l1 - l2) > 3):
            return False
    return True

def check_decr(levels: list):
    for i in range(len(levels) - 1):
        l1, l2 = levels.iloc[i], levels.iloc[i + 1]
        if (l1 <= l2 or abs(l1 - l2) > 3):
            return False
    return True


def part1():
    reports = parse_input()
    inc = reports.apply(check_inc, axis=1)
    decr = reports.apply(check_decr, axis=1)
    n_safe = sum(inc | decr)
    print(n_safe)

part1()


#######################################################################
# Part 2

def check_inc(levels, can_dampen=1):
    for i in range(len(levels) - 1):
        l1, l2 = levels.iloc[i], levels.iloc[i + 1]
        if (l1 >= l2 or abs(l1 - l2) > 3):
            if not can_dampen:
                return False
            can_dampen -= 1
            return (check_inc(levels.drop(i+1), can_dampen=0) 
                    or check_inc(levels.drop(i), can_dampen=0)
                    or (check_inc(levels.drop(i-1), can_dampen=0) if i > 0 else False))
    return True

def check_decr(levels, can_dampen=1):
    for i in range(len(levels) - 1):
        l1, l2 = levels.iloc[i], levels.iloc[i + 1]
        if (l1 <= l2 or abs(l1 - l2) > 3):
            if not can_dampen:
                return False
            can_dampen -= 1
            return (check_decr(levels.drop(i+1), can_dampen) 
                    or check_decr(levels.drop(i), can_dampen)
                    or (check_decr(levels.drop(i-1), can_dampen) if i > 0 else False))
    return True


def part2():
    reports = parse_input()
    inc = reports.apply(check_inc, axis=1)
    decr = reports.apply(check_decr, axis=1)
    n_safe = sum(inc | decr)
    print(n_safe)


part2()