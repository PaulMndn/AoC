with open("2022/res/day_16.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]


import re

class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections
        self.opened = False
    
    def link_connections(self, all_valves):
        self.connections = [all_valves[name] for name in self.connections]

valves = {}
pattern = re.compile(r"^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels lead to valves (.+)$")
for line in input:
    n, fr, conns = re.match(pattern, line)
    valve = Valve(n, int(fr), conns.split(", "))
    valves[n] = valve

for v in valves.values():
    v.link_connections(valves)


# TODO: reduce Network. remove all 0-Valves, connect paths to previous valve(s)


current_minute = 1
max_release = 0
to_check = []
current_valve = valve["AA"]

current_release = 0
while to_check:
    if current_minute > 30:    # carefull, +- 1 error
        if current_release > max_release:
            max_release = current_release
        current_release = 0
        break
    # vlt. doch recursiv machen? states an den jeweiligen nodes merken,
    # wie die bis dahin vergangene Zeit/current_release... 
    




flow_per_minute = []
open_valves = []
for minute in range(1, 31):
    flow_per_minute.append(sum(v.flow_rate for v in open_valves))