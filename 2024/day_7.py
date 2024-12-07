from pathlib import Path

res = Path("./2024/res")


def parse_input():
    with open(res / "day_7.txt") as f:
        lines =  f.readlines()
    eqs = []
    for line in lines:
        line = line.strip().split(" ")
        line = [int(i.strip(": ")) for i in line]
        line = (line[0], line[1:])
        eqs.append(line)
    return eqs


def valid_equation(eq):
    v, term = eq
    if len(term) == 1:
        return v == term[0]
    
    term_plus = [term[0] + term[1]] + term[2:]
    term_mul = [term[0] * term[1]] + term[2:]
    term_concat = [int(str(term[0]) + str(term[1]))] + term[2:]
    return (valid_equation((v, term_plus)) 
            + valid_equation((v, term_mul))
            + valid_equation((v, term_concat)))

def res():
    eqs = parse_input()
    total = 0
    for eq in eqs:
        if valid_equation(eq):
            total += eq[0]
    print(total)

res()