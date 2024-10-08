with open("2022/res/day_7.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
    
    def get_size():
        raise NotImplementedError

class File(Node):
    def __init__(self, name, parent, size):
        self.size = int(size)
        super().__init__(name, parent)
    
    def get_size(self):
        return self.size


class Dir(Node):
    def get_size(self):
        size = sum(i.get_size() for i in self.contents)
        return size



root = Dir("/", None)
current_dir = root

for line in input[1:]:
    parts = line.split(" ")
    
    if parts[0] == "$":
        if parts[1] == "ls":
            continue
        if parts[1] == "cd":
            if parts[2] == "..":
                current_dir = current_dir.parent
                continue

            d = next(i for i in current_dir.contents if i.name == parts[2])
            current_dir = d
    
    else:
        if parts[0] == "dir":
            current_dir.contents.append(Dir(parts[1], current_dir))
        else:
            current_dir.contents.append(File(parts[1], current_dir, parts[0]))

to_check = [root]
small_dirs = []

while len(to_check):
    dir = to_check.pop()
    if dir.get_size() <= 100000:
        small_dirs.append(dir)
    to_check += list(filter(lambda c: isinstance(c, Dir), dir.contents))

total = sum(i.get_size() for i in small_dirs)
print(total)


space_total = 70000000
space_free = space_total - root.get_size()
space_need = 30000000
space_min_del = space_need - space_free

to_check = [root]
enough_dirs = []

while len(to_check):
    dir = to_check.pop()
    if dir.get_size() < space_min_del:
        continue
    enough_dirs.append(dir)
    to_check += list(filter(lambda c: isinstance(c, Dir), dir.contents))

enough_dirs = sorted(enough_dirs, key = lambda x: x.get_size())
print(enough_dirs[0].get_size())
