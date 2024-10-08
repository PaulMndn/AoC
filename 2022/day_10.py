with open("2022/res/day_10.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


register = [1]

def addx(n):
    global register
    register.append(register[-1])
    register.append(register[-1]+n)

def noop():
    global register
    register.append(register[-1])

for line in input:
    if line.startswith("noop"):
        noop()
    elif line.startswith("addx"):
        val = int(line.split()[1])
        addx(val)
    else:
        print(f"Fehler: {line}")

sum = 0
for i in range(19, 220, 40):
    sum += (i+1) * register[i]

print(sum)
print(len(register))

screen = []
line = []
for px, sprite_pos in enumerate(register):
    px = px % 40
    if sprite_pos-1 <= px <= sprite_pos+1:
        line.append("#")
    else:
        line.append(".")

    if len(line) == 40:
        screen.append(line)
        line = []

print("\n".join("".join(l) for l in screen))
