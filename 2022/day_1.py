with open("2022/res/day_1.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]

elves = []
elf = 0
for food in input:
    if food == "":
        elves.append(elf)
        elf = 0
        continue
    elf += int(food)

elves.sort(reverse=True)

print(sum(elves[:3]))

