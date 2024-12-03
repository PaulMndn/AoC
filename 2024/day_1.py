from pathlib import Path

res = Path("./2024/res")

def parse_input():
    l1 = []
    l2 = []
    with open(res / "day_1.txt") as f:
        for line in f:
            line = line.strip()
            nums = line.split('   ')
            l1.append(int(nums[0]))
            l2.append(int(nums[1]))
    return l1, l2

def part1():
    l1, l2 = parse_input()
    l1 = sorted(l1)
    l2 = sorted(l2)
    tot_dist = 0
    for i, j in zip(l1, l2):
        tot_dist += abs(i - j)
    print(tot_dist)

def part2():
    l1, l2 = parse_input()
    sim = 0
    for i in l1:
        count = l2.count(i)
        sim += i * count
    print(sim)


part1()
part2()