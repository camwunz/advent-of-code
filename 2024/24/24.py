from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "24/newinput.txt"
# POSSIBLE SWAPS
# x14 AND y14 = z14


# 14XOR XOR ndq -> vhm

# 27XOR XOR kqj -> mps
# 27AND OR snv -> z27

# 39XOR XOR gpm -> msq
# 39XOR AND gpm -> z39

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def output(base_regs, instructions, filename):
    f = open(filename, 'w')
    for k, v in base_regs.items():
        f.write(f"{k}: {v}\n") 
    f.write("\n")
    for a, action, b, c in instructions:
        f.write(f"{a} {action} {b} -> {c}\n")
    f.close()   

def custom_sort(instruction, order):
    a1, action1, b1, c1 = instruction
    vals = sorted([a1, b1])
    if vals[0][0] == 'x':
        return -1
    else:
        if a1 in order:
            return order.index(a1)
        if b1 in order:
            return order.index(b1)
        return float('inf')

def run(regs, instructions, possible_z):
    regs = regs.copy()
    seen = set()
    while len(seen) != len(instructions):
        new_seen = set()
        for i, (a, action, b, c) in enumerate(instructions):
            if i not in seen:
                if a in regs and b in regs:
                    if action == "OR":
                        regs[c] = 1 if regs[a] == 1 or regs[b] == 1 else 0
                    elif action == "AND":
                        regs[c] = 1 if regs[a] == 1 and regs[b] == 1 else 0
                    elif action == "XOR":
                        regs[c] = 1 if regs[a] != regs[b] else 0
                    new_seen.add(i)
        if not new_seen:
            return False
        seen |= new_seen

    zs = [x for x in regs if x[0] == "z"]
    zs = sorted(zs, reverse=True)
    b = ""
    for z in zs:
        b = b + str(regs[z])
    # print(b)
    if b == possible_z:
        return True
    return False


def main(lines):
    res = 0

    regs = defaultdict(int)
    i = 0
    load = True
    instructions = []
    zs = set()
    order_of_next = []
    forced_swaps = [('vhm', 'z14'), ('mps', 'z27'), ('msq', 'z39'), ('qwf', 'cnk')]
    while i < len(lines):
        if lines[i] == "":
            load = False
            i += 1
        if load:
            name, am = lines[i].split(':')
            am = int(am)
            regs[name] = am
        else:
            a, action, b, _, c = lines[i].split()
            a, b = sorted([a, b])
            instructions.append([a, action, b, c])
            if c[0] == 'z':
                zs.add(c)

        i += 1
    
    for i in range(len(instructions)):
        for j in range(i+1, len(instructions)):
            a1, action1, b1, c1 = instructions[i]
            a3, action1, b2, c2 = instructions[j]
            x, y  = sorted([c1, c2])
            for pa, pb in forced_swaps:
                if pa == x and pb == y:
                    instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]
                    print(instructions[i])
                    print(instructions[j])


    xb = ""
    xs = [x for x in regs if x[0] == 'x']
    for x_name in sorted(xs, reverse=True):
        xb = xb + str(regs[x_name])
    print('x')
    print(xb)


    yb = ""
    ys = [x for x in regs if x[0] == 'y']
    for y_name in sorted(ys, reverse=True):
        yb = yb + str(regs[y_name])
    print('y')
    print(yb)
    z_match = bin(int(xb, 2) + int(yb, 2))[2:]
    print(len(instructions))

    print(f"z should be :\n{z_match}")


    for i in range(len(instructions)):
        print(i, len(instructions))
        for j in range(i+1, len(instructions)):
            instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]
            if run(regs, instructions, z_match):
                print(instructions[j][3], instructions[i][3])
                print("DONEEE")
            instructions[i][3], instructions[j][3] = instructions[j][3], instructions[i][3]


    return res

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    res = main(lines)
    if res is not None:
        print(res)
    print()
    # real input
    input("waiting for input...")
    print("REAL INPUT")
    res = main(data.splitlines())
    if res is not None:
        print(res)
        to_submit = input("Would you like to submit? (y/n): ").strip().lower()
        if to_submit == "y":
            print("\x1B[3mSubmitting...\x1B[0m")
            submit(res, reopen=False)
        else:
            print("\x1B[3mNot submitting...\x1B[0m")
    else:
        print("\x1B[3mNo answer returned, not submitting\x1B[0m")
