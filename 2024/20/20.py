from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from copy import deepcopy
from aocd import submit, data

FILENAME = "20/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

ns = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def dists(lines):
    s = None
    e = None
    for ri in range(len(lines)):
        for ci in range(len(lines[0])):
            if lines[ri][ci] == "S":
                s = (ri, ci)
            if lines[ri][ci] == "E":
                e = (ri, ci)
    
    costs = {s: 0}
    states = deque([(*s, 0)])
    while states:
        r, c, cost = states.popleft()
        for dx, dy in ns:
            nr, nc = r+dx, c+dy
            if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]):
                if (nr, nc) in costs or lines[nr][nc] == "#":
                    continue
                if (nr, nc) == e:
                    costs[(nr, nc)] = cost + 1
                    return costs
                states.append((nr, nc, cost+1))
                costs[(nr, nc)] = cost + 1
    return costs

def main(lines):
    res = 0
    lines = [list(x) for x in lines]
    base_costs = dists(lines)
    # print(base_costs)
    teleports = set()
    dots = set()
    for ri in range(len(lines)):
        for ci in range(len(lines[0])):
            if lines[ri][ci] != "#":
                dots.add((ri, ci))
    print(len(dots))
    for a, b in dots:
        for c, d in dots:
            if abs(c-a) + abs(d-b) <= 20:
                teleports.add(((a,b), (c,d)))

    print(len(teleports))
    counts = defaultdict(int)
    for (a, b), (c, d) in teleports:
        start_cost = base_costs[(a, b)]
        end = base_costs[(c, d)]
        move_cost = abs(c-a) + abs(d-b)
        savings = (end - start_cost - move_cost)
        if savings >= 100:
            res += 1
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
