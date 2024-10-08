with open("2022/res/day_4.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]

count = 0
for pair in input:
    elves = pair.split(",")
    secs = []
    for elf in elves:
        sec = [int(i) for i in elf.split("-")]
        secs.append(set(i for i in range(sec[0], sec[1]+1)))
    
    if secs[0] <= secs[1] or secs[0] >= secs[1]:
        count += 1

print(count)

count = 0
for pair in input:
    elves = pair.split(",")
    secs = []
    for elf in elves:
        sec = [int(i) for i in elf.split("-")]
        secs.append(set(i for i in range(sec[0], sec[1]+1)))
    
    if secs[0].intersection(secs[1]):
        count += 1

print(count)