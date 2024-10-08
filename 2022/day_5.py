with open("2022/res/day_5.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]

import re
from copy import deepcopy

stacks_original = [
    ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
    ["D", "Q", "L"],
    ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
    ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
    ['V', 'G', 'L', 'F', 'Z', 'S'],
    ["D", "G", "N", "P"],
    ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
    ['C', 'P', 'D', 'M', 'S'],
    ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C'],
]

stacks = deepcopy(stacks_original)

def move(frm, to):
    global stacks
    stacks[to-1].append(stacks[frm-1].pop())


for inst in input[10:]:
    match = re.match("move (\d+) from (\d) to (\d)", inst)
    cnt, frm, to = (int(i) for i in match.groups())
    for i in range(cnt):
        move(frm, to)

print("".join(i[-1] for i in stacks))


### Part II ###

stacks = deepcopy(stacks_original)

def move(cnt, frm, to):
    global stacks
    stacks[frm-1], mv = stacks[frm-1][:-cnt], stacks[frm-1][-cnt:]
    stacks[to-1] += mv


for inst in input[10:]:
    match = re.match("move (\d+) from (\d) to (\d)", inst)
    cnt, frm, to = (int(i) for i in match.groups())
    move(cnt, frm, to)

print("".join(i[-1] for i in stacks))

