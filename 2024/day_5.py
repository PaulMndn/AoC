from pathlib import Path
from functools import cmp_to_key

res = Path("./2024/res")


def parse_input():
    with open(res / "day_5.txt") as f:
        lines = f.readlines()
    
    order_rules = {}
    updates = []
    flag = "rules"
    for line in lines:
        line = line.strip()
        if not line:
            flag = "updates"
            continue
        if flag == "rules":
            x, y = line.split("|")
            x, y = int(x), int(y)
            if order_rules.get(x):
                order_rules[x].append(y)
            else:
                order_rules[x] = [y]
        if flag == "updates":
            updates.append([int(i) for i in line.split(",")])
    return order_rules, updates

def order_is_correct(order_rules, update):
    seen = set()
    for i in update:
        if seen.intersection(set(order_rules.get(i, []))):
            return False
        seen.add(i)
    return True

def condense_rules(rules, update):
    update = update.copy()
    condensed = {}
    while len(update):
        i = update.pop(0)
        rules
        

def part1():
    rules, updates = parse_input()
    middle_sum = 0
    for update in updates:
        if order_is_correct(rules, update):
            middle_sum += update[len(update)//2]
    print(middle_sum)

part1()


#######################
# Part 2

def part2():
    rules, updates = parse_input()
    # create rule cache for functools.cmp_to_key()
    rule_cache = {}
    for k, lv in rules.items():
        for v in lv:
            rule_cache[(k, v)] = -1     # correct order
            rule_cache[(v, k)] = 1      # incorrect order
    
    sorted_updates = []
    for update in updates:
        if order_is_correct(rules, update): continue
        update.sort(key=cmp_to_key(lambda x, y: rule_cache.get((x, y), 0)))     # is an in-place function!
        sorted_updates.append(update)   # extract only the updated, previously unordered updates for total calculation
    
    total = 0
    for i in sorted_updates:
        total += i[len(i)//2]
    print(total)

part2()