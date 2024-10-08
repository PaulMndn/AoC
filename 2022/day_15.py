with open("2022/res/day_15.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


import re

class Sensor:
    def __init__(self, pos, pos_beacon):
        self.pos = pos
        self.x, self.y = pos
        self.pos_beacon = pos_beacon
        self.distance = abs(pos_beacon[0]-self.x) + abs(pos_beacon[1]-self.y)


def parse(input, cls):
    out = []
    for line in input:
        regex = r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$"
        groups = re.match(regex, line).groups()
        groups = [int(i) for i in groups]
        out.append(cls((groups[0], groups[1]), (groups[2], groups[3])))
    return out


class Map:
    ICON_SENSOR = "S"
    ICON_BEACON = "B"
    ICON_COVERED = "#"
    ICON_PLACEHOLDER = "."

    def __init__(self):
        self._map = {}
        self.sensors = None
        self.x_range = None
        self.y_range = None
    
    def register_sensors(self, sensors):
        self.sensors = sensors
        for sensor in sensors:
            self._map[sensor.pos] = self.ICON_SENSOR
            self._map[sensor.pos_beacon] = self.ICON_BEACON
        
        # self._mark_covered()
        # coords = self._map.keys()
        # self.x_range = (min(c[0] for c in coords), max(c[0] for c in coords))
        # self.y_range = (min(c[1] for c in coords), max(c[1] for c in coords))
    
    def _mark_covered(self):
        for sensor in self.sensors:
            print(f"{sensor.pos=}")
            for x in range(sensor.distance+1):
                for y in range(sensor.distance - x + 1):
                    pos = (sensor.x + x, sensor.y + y)
                    if self._map.get(pos, None) is None:
                        self._map[pos] = self.ICON_COVERED
                    pos = (sensor.x - x, sensor.y + y)
                    if self._map.get(pos, None) is None:
                        self._map[pos] = self.ICON_COVERED
                    pos = (sensor.x + x, sensor.y - y)
                    if self._map.get(pos, None) is None:
                        self._map[pos] = self.ICON_COVERED
                    pos = (sensor.x - x, sensor.y - y)
                    if self._map.get(pos, None) is None:
                        self._map[pos] = self.ICON_COVERED

    def count_covered_in_line(self, line):
        n = 0
        for x in range(self.x_range[0], self.x_range[1]):
            n += 1 if self._map.get((x, line)) == self.ICON_COVERED else 0
        return n
    
    def print(self):
        for y in range(self.y_range[0], self.y_range[1]+1):
            self.print_line(y)
    
    def print_line(self, y):
        ln = []
        for x in range(self.x_range[0], self.x_range[1]+1):
            ln.append(self._map.get((x,y), self.ICON_PLACEHOLDER))
        print("".join(ln))


sensors = parse(input, Sensor)

# map = Map()
# map.register_sensors(sensors)
# num = map.count_covered_in_line(2_000_000)
# print(num)
line = 2_000_000
x_covered = {}
for s in sensors:
    if line not in range(s.y-s.distance, s.y+s.distance+1):
        continue
    width = s.distance - abs(line - s.y)
    for x in range(s.x-width, s.x+width+1):
        if x not in x_covered:
            x_covered[x] = "#"
    if s.y == line:
        x_covered[s.x] = "S"
    if s.pos_beacon[1] == line:
        x_covered[s.pos_beacon[0]] = "B"

count = 0
for x in x_covered.values():
    if x == "#":
        count+=1
print(count)




##### PART 2 #####

class Sensor2(Sensor):
    def range_on_line(self, y):
        if not (self.y-self.distance <= y <= self.y+self.distance):
            return 
        width = self.distance - abs(y - self.y)
        return self.x-width, self.x+width


sensors = parse(input, Sensor2)
sensors = sorted(sensors, key = lambda s: s.y)
LIMITS = (0, 4000000)

def check_line(y):
    s_intersect = []
    for s in sensors:
        if s.y-s.distance <= y <= s.y+s.distance:
            s_intersect.append(s)
    s_intersect = sorted(s_intersect, key = lambda s: s.range_on_line(y)[0])
    rng = None
    for s in s_intersect:
        s_rng = s.range_on_line(y)
        if s_rng[1] < LIMITS[0]:
            # below range
            continue
        if rng is None:
            # beginning of range
            if s_rng[0] <= LIMITS[0]:
                rng = (LIMITS[0], s_rng[1])
                continue
            elif s_rng[0] > LIMITS[0]:
                return 0
        
        if s_rng[0] > rng[1]:
            # no overlap, missing point found
            return rng[1]+1
        
        if s_rng[1] > rng[1]:
            # extend range
            rng = rng[0], s_rng[1]
        
        if rng[1] >= LIMITS[1]:
            return
    # if rng[1] < LIMITS[1]:
    #     return rng[1]+1



possible_beacon_pos = []
for y in range(LIMITS[1]+1):
    beacon_x = check_line(y)
    if beacon_x is not None:
        possible_beacon_pos.append((beacon_x, y))

for pos in possible_beacon_pos:
    print(f"beacon coords = {pos}, Freq: {pos[0] * 4000000 + pos[1]}")
