from pathlib import Path
import pandas as pd

res = Path("./2024/res")


def parse_input():
    with open(res / "day_4.txt") as f:
        lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    return pd.DataFrame(matrix)


class Crossword:
    def __init__(self):
        self.matrix = parse_input()
        self.total_count = None
    
    def search0deg(self, y, x):
        if y < 3:
            return False
        df = self.matrix
        if (df.at[y-1, x] == "M" 
            and df.at[y-2, x] == "A"
            and df.at[y-3, x] == "S"):
            return True
        return False

    def search45deg(self, y, x):
        df = self.matrix
        if y < 3 or x > df.shape[1]-4:      # shape -4 because we need 3 characters and shape starts counting at 1 not 0
            return False
        if (df.at[y-1, x+1] == "M" 
            and df.at[y-2, x+2] == "A"
            and df.at[y-3, x+3] == "S"):
            return True
        return False

    def search90deg(self, y, x):
        df = self.matrix
        if x > df.shape[1]-4:
            return False
        if (df.at[y, x+1] == "M" 
            and df.at[y, x+2] == "A"
            and df.at[y, x+3] == "S"):
            return True
        return False

    def search135deg(self, y, x):
        df = self.matrix
        if y > df.shape[0]-4 or x > df.shape[1]-4:
            return False
        if (df.at[y+1, x+1] == "M"
            and df.at[y+2, x+2] == "A"
            and df.at[y+3, x+3] == "S"):
            return True
        return False

    def search180deg(self, y, x):
        df = self.matrix
        if y > df.shape[0]-4:
            return False
        if (df.at[y+1, x] == "M"
            and df.at[y+2, x] == "A"
            and df.at[y+3, x] == "S"):
            return True
        return False

    def search225deg(self, y, x):
        df = self.matrix
        if y > df.shape[0]-4 or x < 3:
            return False
        if (df.at[y+1, x-1] == "M"
            and df.at[y+2, x-2] == "A"
            and df.at[y+3, x-3] == "S"):
            return True
        return False

    def search270deg(self, y, x):
        df = self.matrix
        if x < 3:
            return False
        if (df.at[y, x-1] == "M"
            and df.at[y, x-2] == "A"
            and df.at[y, x-3] == "S"):
            return True
        return False

    def search315deg(self, y, x):
        df = self.matrix
        if y < 3 or x < 3:
            return False
        if (df.at[y-1, x-1] == "M"
            and df.at[y-2, x-2] == "A"
            and df.at[y-3, x-3] == "S"):
            return True
        return False

    def search(self):
        matrix = self.matrix
        y, x = self.matrix.shape
        total = 0
        for i in range(y):
            for j in range(x):
                if matrix.at[i, j] == "X":
                    total += sum([self.search0deg(i, j),
                                  self.search45deg(i, j),
                                  self.search90deg(i, j),
                                  self.search135deg(i, j),
                                  self.search180deg(i, j),
                                  self.search225deg(i, j),
                                  self.search270deg(i, j),
                                  self.search315deg(i, j)])
        self.total_count = total

def part1():
    crossword = Crossword()
    crossword.search()
    print(crossword.total_count)
    

part1()


#######################################################################
# Part 2

class Crossword2:
    def __init__(self):
        self.matrix = parse_input()
        self.total_count = None
        # print(self.matrix)
    
    def search(self):
        matrix = self.matrix
        y, x = self.matrix.shape
        total = 0
        for i in range(1, y-1):     # No need to search the first and last row/column because the "M" is in the middle
            for j in range(1, x-1):
                if matrix.at[i, j] == "A":
                    if (((matrix.at[i-1, j-1] == "M" and matrix.at[i+1, j+1] == "S")
                         or (matrix.at[i-1, j-1] == "S" and matrix.at[i+1, j+1] == "M"))
                        and ((matrix.at[i-1, j+1] == "M" and matrix.at[i+1, j-1] == "S")
                         or (matrix.at[i-1, j+1] == "S" and matrix.at[i+1, j-1] == "M"))):
                        total += 1
        self.total_count = total

def part2():
    crossword = Crossword2()
    crossword.search()
    print(crossword.total_count)

part2()
