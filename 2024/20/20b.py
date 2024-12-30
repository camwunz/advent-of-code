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
    teleports = set()
    dots = set()
    for ri in range(len(lines)):
        for ci in range(len(lines[0])):
            if lines[ri][ci] != "#":
                dots.add((ri, ci))
    
    for a, b in dots:
        for c in range(a-22, a+22):
            for d in range(b-22, b+22):
                if (c, d) in dots:
                    if a != c and b != d:
                        dx = abs(c-a)
                        x_direction = int((c-a)/dx)
                        dy = abs(d-b)
                        y_direction = int((d-b)/dy)
                        if dx:
                            can_go_startx = lines[a+x_direction][b] != "#"
                            can_go_endx = lines[c-x_direction][d] != "#"
                        if dy:
                            can_go_starty = lines[a][b+y_direction] != '#'
                            can_go_endy = lines[c][d-y_direction] != "#"
                        # if dx and dy:
                        #     if (can_go_startx and can_go_starty):
                        #         continue
                        #     if (can_go_endx and can_go_endy):
                        #         continue
                        # elif dx and not dy:
                        #     if can_go_startx or can_go_endx:
                        #         continue
                        # elif dy and not dx:
                        #     if can_go_starty or can_go_endy:
                        #         continue
                        if abs(c-a) + abs(d-b) <= 20:
                            teleports.add(((a,b), (c,d)))

    print(len(teleports))
    for (a, b), (c, d) in teleports:
        start_cost = base_costs[(a, b)]
        end = base_costs[(c, d)]
        move_cost = abs(c-a) + abs(d-b)
        if (end - start_cost - move_cost) >= 70:
            # print(a, b, c, d)
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
