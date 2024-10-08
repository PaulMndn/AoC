with open("2022/res/day_9.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dir):
        dx = dy = 0
        match dir:
            case "R": dx = +1
            case "U": dy = +1
            case "L": dx = -1
            case "D": dy = -1
        return Cursor(self.x +dx, self.y +dy)
    
    def go_step(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        # normalize:
        dx = dx if dx == 0 else dx//abs(dx)
        dy = dy if dy == 0 else dy//abs(dy)
        return Cursor(self.x + dx, self.y + dy)
    
    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        if (abs(dx) == 1 and abs(dy) <=1) or (abs(dy) == 1 and abs(dx) <= 1):
            return 1
        if other.x == self.x and other.y == self.y:
            return 0
        
        return 1+ self.go_step(other).distance_to(other)

head = Cursor(0,0)
tail = Cursor(0,0)

visited = {(0,0)}

for line in input:
    dir, steps = line.split(" ")
    for step in range(int(steps)):
        head = head.move(dir)
        if tail.distance_to(head) > 1:
            tail = tail.go_step(head)
            visited.add((tail.x, tail.y))

print(len(visited))
