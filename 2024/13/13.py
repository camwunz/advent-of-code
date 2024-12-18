from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "13/input.txt"
ns = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0

    machines = []
    i = 0
    while i < len(lines):
        new_machine = {'a': (0, 0), 'b': (0, 0), 'prize': (0, 0)}
        ax, ay = [int(x.split("+")[1]) for x in lines[i].split(":")[1].split(",")]
        i += 1
        bx, by = [int(x.split("+")[1]) for x in lines[i].split(":")[1].split(",")]
        i += 1
        px = int(lines[i].split("=")[1].split(",")[0])  + 10000000000000
        py = int(lines[i].split("=")[-1])  + 10000000000000
        new_machine['a'] = (ax, ay)
        new_machine['b'] = (bx, by)
        new_machine['prize'] = (px, py)
        print(new_machine)
        i += 2
        machines.append(new_machine)
    
    for machine in machines:
        ax, ay = machine['a']
        bx, by = machine['b']
        px, py = machine['prize']
        a1 = (px * by - py * bx) / (ax*by - ay * bx)
        axres = ax * a1
        ayres = ay * a1
        bxres = (px - axres) / bx
        byres = (py - ayres) / by
        cost = 3 * a1 + bxres
        print(axres, ayres, bxres, cost)
        if axres.is_integer() and bxres.is_integer() and axres > 0 and bxres > 0:
            print('added')
            res += cost


    return res

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    # res = main(lines)
    # if res is not None:
    #     print(res)
    # print()
    # # real input
    # input("waiting for input...")
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
