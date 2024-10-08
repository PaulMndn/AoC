with open("2022/res/day_3.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


def get_prio(t):
    temp = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return temp.index(t)+1



mixups = ""

for r in input:
    half = len(r)//2
    comp1, comp2 = r[:half], r[half:]

    for t in comp1:
        if t in comp2:
            mixups += t
            break

sum = 0
for t in mixups:
    sum += get_prio(t)

print(sum)

sum = 0
for i in range(0, len(input), 3):
    group = input[i:i+3]
    badge = set(group[0]).intersection(group[1]).intersection(group[2])
    sum += get_prio(list(badge)[0])

print(sum)
