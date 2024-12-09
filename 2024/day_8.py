from pathlib import Path
from copy import deepcopy

res = Path("./2024/res")


def parse_input():
    with open(res / "day_8.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid

class Grid:
    def __init__(self):
        self.grid = parse_input()
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.antennas_by_freq = {}
        self.antinodes = set()

        self._load_antenna_positions()
    
    def _load_antenna_positions(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == ".": continue
                
                if cell not in self.antennas_by_freq:
                    self.antennas_by_freq[cell] = [(i, j)]
                else:
                    self.antennas_by_freq[cell].append((i, j))

    def _is_inbounds(self, pos):
        if 0 <= pos[0] < self.height and 0 <= pos[1] < self.width:
            return True
        return False
    
    def _get_antinodes_of_pair(self, ant_a, ant_b):
        dy, dx = ant_b[0] - ant_a[0], ant_b[1] - ant_a[1]
        node_a = (ant_a[0] - dy, ant_a[1] - dx)
        node_b = (ant_b[0] + dy, ant_b[1] + dx)
        ret = set()
        if self._is_inbounds(node_a):
            ret.add(node_a)
        if self._is_inbounds(node_b):
            ret.add(node_b)
        return ret
    
    def get_unique_antinodes(self):
        for positions in self.antennas_by_freq.values():
            if len(positions) < 2:
                # only one antenna of this frequency. No antinodes.
                continue
            for i, ant_a in enumerate(positions):
                for ant_b in positions[i + 1:]:
                    self.antinodes.update(self._get_antinodes_of_pair(ant_a, ant_b))
        return self.antinodes
    
    def print(self, include_antinodes=False):
        if include_antinodes() and not self.antinodes:
            self.get_unique_antinodes()
        print_grid = deepcopy(self.grid)
        for i in self.antinodes:
            if print_grid[i[0]][i[1]] == ".":
                print_grid[i[0]][i[1]] = "#"
        for row in print_grid:
            print("".join(row))
            

def part1():
    grid = Grid()
    print(len(grid.get_unique_antinodes()))

part1()


class Grid2(Grid):
    def _get_antinodes_of_pair(self, ant_a, ant_b):
        dy, dx = ant_b[0] - ant_a[0], ant_b[1] - ant_a[1]
        
        ret = set()
        factor = 0
        while True:
            node_a = (ant_a[0] - factor * dy, ant_a[1] - factor * dx)
            if not self._is_inbounds(node_a):
                break
            ret.add(node_a)
            factor += 1
        
        factor = 0
        while True:
            node_b = (ant_b[0] + factor * dy, ant_b[1] + factor * dx)
            if not self._is_inbounds(node_b):
                break
            ret.add(node_b)
            factor += 1
        
        return ret

def part2():
    grid = Grid2()
    print(len(grid.get_unique_antinodes()))

part2()