with open("2022/res/day_13.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


import itertools

def calc(left, right):
    
    # compare ints
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return -1
        elif left < right:
            return 1
        elif left == right:
            return 0
    
    # terminal conds. for list running out
    if right is None:
        return -1
    if left is None:
        return 1
    
    # only one list, put other in list as well
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    if isinstance(right, list) and isinstance(left, int):
        left = [left]
    
    if isinstance(left, list) and isinstance(right, list):
        for new_left, new_right in itertools.zip_longest(left, right):
            c = calc(new_left, new_right)
            if c != 0:
                return c
        return 0


res = {}
for i in range(0, len(input), 3):
    l, r = input[i: i+2]
    l, r = eval(l), eval(r)
    res[i//3+1] = True if calc(l, r) == 1 else False

print(sum(k for k, v in res.items() if v))



##### PART 2 #####

class Pkg:
    def __init__(self, pkg: list):
        self.pkg = pkg
    
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__class__.__name__} with {other.__class__.__name__}.")
        return calc(self.pkg, other.pkg) == 1
        
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__class__.__name__} with {other.__class__.__name__}.")
        return calc(self.pkg, other.pkg) == -1
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can't compare {self.__class__.__name__} with {other.__class__.__name__}.")
        return calc(self.pkg, other.pkg) == 0
    

DIVIDER_PKGS = [Pkg([[2]]), Pkg([[6]])]

input = list(filter(lambda l: bool(l), input))
input = [Pkg(eval(l)) for l in input] + DIVIDER_PKGS

result = sorted(input)
div_pkg_indices = [result.index(p)+1 for p in DIVIDER_PKGS]
print(div_pkg_indices[0] * div_pkg_indices[1])
