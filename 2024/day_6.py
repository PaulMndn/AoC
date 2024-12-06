from pathlib import Path
from pprint import pprint
import time

res = Path("./2024/res")


def parse_input():
    with open(res / "day_6.txt") as f:
        grid = f.readlines()
    grid = [list(l.strip()) for l in grid]
    return grid


class Guard:
    def __init__(self, map):
        self.map = map
        self.in_loop = False
        self.pos = self._get_pos_from_grid()
        
        self.seen = {self.pos}
    
    def _get_pos_from_grid(self, delete_pos=True):
        grid = self.map.grid
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "^":
                    if delete_pos:
                        row[x] = "."
                    return (y, x, -1, 0)
        raise ValueError("No guard found")
    
    def has_left(self):
        y, x, _, _ = self.pos
        if x in range(self.map.width) and y in range(self.map.height):
            return False
        return True
    
    def _turn_right(self):
        rightturn = {
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0)
        }
        y, x, dy, dx = self.pos
        dy, dx = rightturn[(dy, dx)]
        self.pos = y, x, dy, dx
    
    def _step_forward(self):
        y, x, dy, dx = self.pos
        self.pos = (y+dy, x+dx, dy, dx)
            
    def _path_loops(self):
        if self.pos in self.seen:
                return True
        return False

    def step(self):
        map = self.map
        y, x, dy, dx = self.pos
        new_coord = (y + dy, x + dx)
        
        if map.is_obsturcted(new_coord):
            self._turn_right()
        else:
            self._step_forward()
        
        if self._path_loops():
            self.in_loop = True
        
        if not self.map.is_out_of_bounds(self.pos):
            # don't care about any positions the guard has visited outside the grid
            self.seen.add(self.pos)


class Map:
    def __init__(self, grid):
        # self.og_grid = grid.copy()
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        
        self.guard = Guard(self)
    
    def is_obsturcted(self, pos):
        y, x = pos
        if y not in range(self.height) or x not in range(self.width):
            # assume no obstructions outside grid
            return False
        return self.grid[pos[0]][pos[1]] in "#O"
    
    def is_out_of_bounds(self, pos):
        y, x, _, _ = pos
        return y not in range(self.height) or x not in range(self.width)
    
    def place_obstruction(self, pos):
        y, x = pos
        if self.is_obsturcted(pos) or pos == self.guard.pos:
            return False
        self.grid[y][x] = "O"
    
    def hard_reset(self):
        return Map(parse_input())

    def step(self):
        self.guard.step()
    
    def step_until_guard_leaves_or_loops(self, visualize=False, dt=0.2):
        while not self.guard.has_left() and not self.guard.in_loop:
            self.step()
            if visualize:
                self.print(guard_visits=True, guard=True)
                time.sleep(dt)

    
    def print(self, guard_visits=False, guard=False):
        grid = self.grid

        if guard_visits:
            for pos in self.guard.seen:
                y, x, _, _ = pos
                try:
                    grid[y][x] = "X"
                except IndexError:
                    continue
        
        if guard and not self.guard.has_left():
            y, x, dy, dx = self.guard.pos
            match (dy, dx):
                case (-1, 0):
                    icon = "^"
                case (0, 1):
                    icon = ">"
                case (1, 0):
                    icon = "v"
                case (0, -1):
                    icon = "<"
            try:
                grid[y][x] = icon
            except IndexError:
                pass
        
        s = ["".join(r) for r in grid]
        s = "\n".join(s)
        print(s)
        print("\n\n")

##############################
# Part 1

def part1():
    map = Map(parse_input())
    map.step_until_guard_leaves_or_loops(visualize=False)
    print(len(map.guard.seen))

# part1()
# visualize_part1()

##############################
# Part 2

def part2():
    map = Map(parse_input())
    map.step_until_guard_leaves_or_loops()
    default_guard_cells = {(y, x) for y, x, _, _ in map.guard.seen}
    print(f"{len(default_guard_cells)} possible cells to obstruct")

    looping_maps = []
    for i, pos in enumerate(default_guard_cells):
        if i%100 == 0:
            print(f"Placing obstruction number {i}/{len(default_guard_cells)}")
        obs_pos = pos[:2]
        # print(f"Placing obstructions number {i}/{len(default_guard_cells)} at {obs_pos}")
        map = Map(parse_input())        # load fresh map to place obstruction
        map.place_obstruction(obs_pos)
        map.step_until_guard_leaves_or_loops(visualize=False, dt=.03)

        # print(f"Guard visited {len(map.guard.seen)} cells and {"looped" if map.guard.in_loop else "left"}")
        if map.guard.in_loop:
            looping_maps.append(map)
        
    
    # for map in looping_maps:
    #     map.print()

    # print(obstructions_to_loop)
    print(len(looping_maps))
    
part2()