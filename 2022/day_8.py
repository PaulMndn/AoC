with open("2022/res/day_8.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]

map = []
for line in input:
    map.append([int(t) for t in line])

width = len(map[0])
height = len(map)

def is_visible(x, y):
    if x == 0 or y == 0 or x == width-1 or y == height-1:
        return True
    
    # visible from left
    for i in range(x):
        if map[y][i] >= map[y][x]:
            break
    else:
        return True
    
    # visible from right
    for i in range(width-1, x, -1):
        if map[y][i] >= map[y][x]:
            break
    else:
        return True
    
    # visible from top
    for i in range(0, y):
        if map[i][x] >= map[y][x]:
            break
    else:
        return True
    
    # visible from bottom
    for i in range(height-1, y, -1):
        if map[i][x] >= map[y][x]:
            break
    else:
        return True
    
    return False


count = 0
for y in range(height):
    for x in range(width):
        if is_visible(x, y):
            count += 1

print(count)


def scenic_score(x, y):
    # look right:
    right = 0
    for i in range(x+1, width):
        right += 1
        if map[y][i] >= map[y][x]:
            break
    
    # look left:
    left = 0
    for i in range(x-1, -1, -1):
        left += 1
        if map[y][i] >= map[y][x]:
            break
    
    # look down:
    down = 0
    for i in range(y+1, height):
        down += 1
        if map[i][x] >= map[y][x]:
            break
    
    # look up:
    up = 0
    for i in range(y-1, -1, -1):
        up += 1
        if map[i][x] >= map[y][x]:
            break
    
    return right * left * down * up


max_scene = 0

for y in range(height):
    for x in range(width):
        scene = scenic_score(x, y)
        if scene > max_scene:
            max_scene = scene

print(max_scene)