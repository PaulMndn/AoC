with open("2022/res/day_12.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


LEGEND = {l: i for i,l in enumerate("abcdefghijklmnopqrstuvwxyz")}
LEGEND["S"] = 0
LEGEND["E"] = 25
START_COORDS = (0, 20)
END_COORDS = (137, 20)
X_MAX = 161
Y_MAX = 40
MAP = [[pos for pos in line] for line in input]


class Node:
    def __init__(self, pos: tuple, g_cost: int):
        self.position = pos
        self.x, self.y = pos
        self.g_cost = g_cost
        self.height = MAP[self.y][self.x]
        match self.height:
            case "S": self.height = "a"
            case "E": self.height = "z"
        self.h_cost = self._approx_h_cost()
        
        self.f_cost = self.g_cost + self.h_cost
    
    def _approx_h_cost(self):
        delta_s = abs(END_COORDS[0]-self.position[0]) + abs(END_COORDS[1]-self.position[1])
        delta_height = LEGEND['z'] - LEGEND[self.height]
        return max(delta_s, delta_height)
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.position == other.position
    
    def discover(self):
        neighbors = []
        if self.x <= X_MAX-1:
            if n := self.get_neighbour(self.x+1, self.y):
                neighbors.append(n)
        if self.x >= 1:
            if n := self.get_neighbour(self.x-1, self.y):
                neighbors.append(n)
        if self.y <= Y_MAX-1:
            if n := self.get_neighbour(self.x, self.y+1):
                neighbors.append(n)
        if self.y >= 1:
            if n := self.get_neighbour(self.x, self.y-1):
                neighbors.append(n)
        return neighbors
    
    def get_neighbour(self, x, y):
        if LEGEND[MAP[y][x]] > LEGEND[self.height]+1:
            return False
        return Node(pos=(x,y), g_cost=self.g_cost+1)


start = Node(pos=START_COORDS, g_cost=0)
to_check = [start]
checked = []

while to_check:
    to_check = sorted(to_check, key=lambda n: n.f_cost)
    current_node: Node = to_check.pop(0)
    # print(f"{current_node.position=}")
    if current_node.position == END_COORDS:
        break
    if current_node in checked:
        continue

    to_check += current_node.discover()
    checked.append(current_node)

print(f"F-Cost: {current_node.f_cost}, G-Cost: {current_node.g_cost}, H-Cost: {current_node.h_cost}")



##### PART 2 #####

class NodeB(Node):
    def _approx_h_cost(self):
        return abs(LEGEND['a'] - LEGEND[self.height])
    
    def get_neighbour(self, x, y):
        if LEGEND[MAP[y][x]] < LEGEND[self.height]-1:
            return False
        return NodeB(pos=(x,y), g_cost=self.g_cost+1)


start = NodeB(pos=END_COORDS, g_cost=0)
to_check = [start]
checked = []

while to_check:
    to_check = sorted(to_check, key=lambda n: n.f_cost)
    current_node: NodeB = to_check.pop(0)
    print(f"{current_node.height=} {current_node.position=}")
    if current_node.height == "a":
        break
    if current_node in checked:
        continue

    to_check += current_node.discover()
    checked.append(current_node)

print(f"F-Cost: {current_node.f_cost}, G-Cost: {current_node.g_cost}, H-Cost: {current_node.h_cost}")
