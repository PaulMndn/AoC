with open("2022/res/day_2.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


def parse(x):
    if x in "AX":
        # rock / loose
        return 0
    if x in "BY":
        # paper / draw
        return 1
    if x in "CZ":
        # scissors / win
        return 2


score = 0

for round in input:
    o, res = round.split()
    o = parse(o)
    res = parse(res)-1

    p = (o + res) % 3

    if o == p:
        # draw
        score += 3
    elif (o + 1)%3 == p:
        score += 6
    
    score += p+1

print(score)