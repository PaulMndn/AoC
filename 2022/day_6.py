with open("2022/res/day_6.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]

s = input[0]
for i in range(len(s)):
    chunk = s[i:i+4]
    if len(set(chunk)) == 4:
        print(i+4)
        break

for i in range(len(s)):
    chunk = s[i:i+14]
    if len(set(chunk)) == 14:
        print(i+14)
        break