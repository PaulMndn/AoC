with open("2022/res/day_14.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


class Cave:
    ROCK = "#"
    AIR = "."
    SAND = "o"
    SAND_ORI = (500,0)
    def __init__(self, input) -> None:
        self.slice = {}
        self._parse_input(input)
        self.min_x = min(coord[0] for coord in self.slice)
        self.max_x = max(coord[0] for coord in self.slice)
        self.min_y = 0
        self.max_y = max(coord[1] for coord in self.slice)
    
    def _parse_input(self, input):
        for line in input:
            prev_node = None
            for node in line:
                if prev_node is None:
                    prev_node = node
                    continue
                self._rock_fill(prev_node, node)
                prev_node = node
    
    def _rock_fill(self, frm, to):
        frm_x, frm_y = frm
        to_x, to_y = to

        # downwards
        if frm_x == to_x:
            endpoints = sorted((frm_y, to_y))
            for i in range(*endpoints):
                self.slice[(frm_x, i)] = self.ROCK
        
        # sideways
        elif frm_y == to_y:
            endpoints = sorted((frm_x, to_x))
            for i in range(*endpoints):
                self.slice[(i, frm_y)] = self.ROCK
        
        # place rock on to-position (excluded in range)
        self.slice[(to_x,to_y)] = self.ROCK
    
    def get_sand_count(self):
        particles = self.slice.values()
        return len(list(filter(lambda p: p == self.SAND, particles)))

    def fill_with_sand(self):
        falls_into_void = False
        while not falls_into_void:
            falls_into_void = self._drop_sand_unit(self.SAND_ORI)

    def _drop_sand_unit(self, pos):
        # out of bounds
        if (pos[0] < self.min_x or pos[0] > self.max_x 
                or pos[1] < self.min_y or pos[1] > self.max_y):
            return True
        
        slice = self.slice
        down = (pos[0], pos[1]+1)
        down_left = (pos[0]-1, pos[1]+1)
        down_right = (pos[0]+1, pos[1]+1)
        
        # check down, down left, and down right and go there
        if slice.get(down) is None:
            return self._drop_sand_unit(down)
        if slice.get(down_left) is None:
            return self._drop_sand_unit(down_left)
        if slice.get(down_right) is None:
            return self._drop_sand_unit(down_right)
        
        # comes to rest
        self.slice[pos] = self.SAND
        return
        '''
        def drop(position):
            position ist stein:
                ret false
            
            success = drop(down)
            wenn success:
                ret true
            success = drop(left)
            wenn success:
                ret true
            success = drop(right)
            wenn success:
                ret true
            
        '''

parsed_input = []
for line in input:
    path = []
    coords = line.split(" -> ")
    for coord in coords:
        path.append(tuple(int(i) for i in coord.split(",")))
    parsed_input.append(path)

cave = Cave(parsed_input)
cave.fill_with_sand()
print(cave.get_sand_count())


##### PART 2 #####

class Cave:
    ROCK = "#"
    AIR = "."
    SAND = "o"
    SAND_ORI = (500,0)
    def __init__(self, input) -> None:
        self.slice = {}
        self._parse_input(input)
        self.min_x = min(coord[0] for coord in self.slice)
        self.max_x = max(coord[0] for coord in self.slice)
        self.min_y = 0
        self.max_y = max(coord[1] for coord in self.slice)
    
    def _parse_input(self, input):
        for line in input:
            prev_node = None
            for node in line:
                if prev_node is None:
                    prev_node = node
                    continue
                self._rock_fill(prev_node, node)
                prev_node = node
    
    def _rock_fill(self, frm, to):
        frm_x, frm_y = frm
        to_x, to_y = to

        # downwards
        if frm_x == to_x:
            endpoints = sorted((frm_y, to_y))
            for i in range(*endpoints):
                self.slice[(frm_x, i)] = self.ROCK
        
        # sideways
        elif frm_y == to_y:
            endpoints = sorted((frm_x, to_x))
            for i in range(*endpoints):
                self.slice[(i, frm_y)] = self.ROCK
        
        # place rock on to-position (excluded in range)
        self.slice[(to_x,to_y)] = self.ROCK
    
    def get_sand_count(self):
        particles = self.slice.values()
        return len(list(filter(lambda p: p == self.SAND, particles)))

    def fill_with_sand(self):
        while True:
            self._drop_sand_unit(self.SAND_ORI)
            if self.slice.get(self.SAND_ORI) == self.SAND:
                break

    def _drop_sand_unit(self, pos):
        # on ground floor
        if pos[1] == self.max_y +1:
            self.slice[pos] = self.SAND
            return
        
        slice = self.slice
        down = (pos[0], pos[1]+1)
        down_left = (pos[0]-1, pos[1]+1)
        down_right = (pos[0]+1, pos[1]+1)
        
        # check down, down left, and down right and go there
        if slice.get(down) is None:
            return self._drop_sand_unit(down)
        if slice.get(down_left) is None:
            return self._drop_sand_unit(down_left)
        if slice.get(down_right) is None:
            return self._drop_sand_unit(down_right)
        
        # comes to rest
        self.slice[pos] = self.SAND
        return


parsed_input = []
for line in input:
    path = []
    coords = line.split(" -> ")
    for coord in coords:
        path.append(tuple(int(i) for i in coord.split(",")))
    parsed_input.append(path)

cave = Cave(parsed_input)
cave.fill_with_sand()
print(cave.get_sand_count())