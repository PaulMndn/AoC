with open("2022/res/day_11.txt", "r") as f:
    input = f.readlines()
input = [l.strip() for l in input]

from datetime import datetime

class Monkey:
    def __init__(self, 
                 name: str,
                 monkeys: list, 
                 items: list, 
                 operation: str, 
                 div_cond: int, 
                 target_true: int, 
                 target_false: int) -> None:
        self.name = name
        self.monkeys = monkeys
        self.items = items
        calc_op, self.calc_num = self._parse_operation(operation)
        self.operation = None
        self.div_cond = div_cond
        self.target_true = target_true
        self.target_false = target_false
        
        self.count_inspections = 0

        match calc_op:
            case "+": self.operation = self._calc_plus
            case "*": self.operation = self._calc_mult
            case "^2": self.operation = self._calc_squared

    @classmethod
    def from_txt(cls, monkeys, lines):
        params = {'monkeys': monkeys}
        for line in lines:
            parts = line.split()
            if line.startswith("Monkey "):
                params['name'] = int(parts[-1].strip(":"))
            elif line.startswith("Starting items: "):
                params['items'] = [int(i.strip(",")) for i in parts[2:]]
            elif line.startswith("Operation: "):
                params['operation'] = " ".join(parts[3:])
            elif line.startswith("Test: "):
                params['div_cond'] = int(parts[-1])
            elif line.startswith("If true: "):
                params['target_true'] = int(parts[-1])
            elif line.startswith("If false: "):
                params['target_false'] = int(parts[-1])
        return cls(**params)
    
    def _parse_operation(self, op):
        parts = op.split()
        operation = parts[-2]
        number = None
        if operation == "*" and parts[-1] == "old":
            operation = "^2"
        else:
            number = int(parts[-1])
        return operation, number
    
    def _calc_plus(self, item, num):
        return item + num
    
    def _calc_mult(self, item, num):
        return item * num
    
    def _calc_squared(self, item, *args, **kwargs):
        return item **2


    def take_turn(self):
        for i in range(len(self.items)):
            item = self.items.pop(0)
            self.work_item(item)
        
    def work_item(self, item):
        item = self.inspect(item)
        item = item // 3    # lose interest, worry goes down
        self.throw_item(item)
    
    def inspect(self, item):
        self.count_inspections += 1
        return self.operation(item, self.calc_num)
            
    def throw_item(self, item):
        if item % self.div_cond == 0:
            self.monkeys[self.target_true].catch(item)
        else:
            self.monkeys[self.target_false].catch(item)
    
    def catch(self, item):
        self.items.append(item)

monkeys = []
for i in range(0, len(input), 7):
    lines = input[i:i+7]
    monkeys.append(Monkey.from_txt(monkeys, lines))

for round in range(20):
    # print(f"{round=} {datetime.now()}")
    for monkey in monkeys:
        monkey.take_turn()


m_sorted = sorted(monkeys, key=lambda m: m.count_inspections, reverse=True)
print("\n".join(f"monkey {m.name} inspected {m.count_inspections} times" 
                for m in m_sorted))
m_business = m_sorted[0].count_inspections * m_sorted[1].count_inspections
print(m_business)

# import sys
# sys.exit()
##### PART 2 #####
class Item:
    MOD_RANGES = [2, 3, 5, 7, 11, 13, 17, 19]
    def __init__(self, value):
        self.values = {}
        for m in self.MOD_RANGES:
            self.values[m] = value % m
    
    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Can't add type {other.__class__.__name__} to {self.__class__.__name__}. Expected: {int.__class__.__name__}")
        for m, val in self.values.items():
            self.values[m] = (val + other) % m
        return self
    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Can't multiply type {self.__class__.__name__} with {other.__class__.__name__}. Expected: {int.__class__.__name__}")
        for m, val in self.values.items():
            self.values[m] = (val * other) % m
        return self
    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Can't divide type {self.__class__.__name__} by {other.__class__.__name__}. Expected: {int.__class__.__name__}")
        for m, val in self.values.items():
            self.values[m] = (val ** other) % m
        return self
    
    def __mod__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Can't modulo type {self.__class__.__name__} with {other.__class__.__name__}. Expected: {int.__class__.__name__}")
        if other not in self.MOD_RANGES:
            raise ValueError(f"Unexpected modulo value. Expected one of: {', '.join(i for i in self.MOD_RANGE)}")
        return self.values[other]
    
    

class Monkey:
    def __init__(self, 
                 name: str,
                 monkeys: list, 
                 items: list, 
                 operation: str, 
                 div_cond: int, 
                 target_true: int, 
                 target_false: int) -> None:
        self.name = name
        self.monkeys = monkeys
        self.items = [Item(i) for i in items]
        calc_op, self.calc_num = self._parse_operation(operation)
        self.operation = None
        self.div_cond = div_cond
        self.target_true = target_true
        self.target_false = target_false
        
        self.count_inspections = 0

        match calc_op:
            case "+": self.operation = self._calc_plus
            case "*": self.operation = self._calc_mult
            case "^2": self.operation = self._calc_squared

    @classmethod
    def from_txt(cls, monkeys, lines):
        params = {'monkeys': monkeys}
        for line in lines:
            parts = line.split()
            if line.startswith("Monkey "):
                params['name'] = int(parts[-1].strip(":"))
            elif line.startswith("Starting items: "):
                params['items'] = [int(i.strip(",")) for i in parts[2:]]
            elif line.startswith("Operation: "):
                params['operation'] = " ".join(parts[3:])
            elif line.startswith("Test: "):
                params['div_cond'] = int(parts[-1])
            elif line.startswith("If true: "):
                params['target_true'] = int(parts[-1])
            elif line.startswith("If false: "):
                params['target_false'] = int(parts[-1])
        return cls(**params)
    
    def _parse_operation(self, op):
        parts = op.split()
        operation = parts[-2]
        number = None
        if operation == "*" and parts[-1] == "old":
            operation = "^2"
        else:
            number = int(parts[-1])
        return operation, number
    
    def _calc_plus(self, item, num):
        return item + num
    
    def _calc_mult(self, item, num):
        return item * num

    def _calc_squared(self, item, *args, **kwargs):
        return item **2


    def take_turn(self):
        while len(self.items):
            item = self.items.pop(0)
            self.work_item(item)
        
    def work_item(self, item):
        item = self.inspect(item)
        # item = item // 3    # lose interest, worry goes down
        self.throw_item(item)
    
    def inspect(self, item):
        self.count_inspections += 1
        return self.operation(item, self.calc_num)
            
    def throw_item(self, item):
        if item % self.div_cond == 0:
            self.monkeys[self.target_true].catch(item)
        else:
            self.monkeys[self.target_false].catch(item)
    
    def catch(self, item):
        self.items.append(item)

monkeys = []
for i in range(0, len(input), 7):
    lines = input[i:i+7]
    monkeys.append(Monkey.from_txt(monkeys, lines))

for round in range(10000):
    # print(f"{round=} {datetime.now()}")
    for monkey in monkeys:
        monkey.take_turn()


m_sorted = sorted(monkeys, key=lambda m: m.count_inspections, reverse=True)
print("\n".join(f"monkey {m.name} inspected {m.count_inspections} times" 
                for m in m_sorted))
m_business = m_sorted[0].count_inspections * m_sorted[1].count_inspections
print(m_business)

