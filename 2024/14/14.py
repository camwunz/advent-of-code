from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "14/input.txt"
ns = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

# SIZE = 11, 7
SIZE = 101, 103

def pr(robots, _):
    print()
    print("NEW", _+1)
    currs = set()
    for (sx, sy), (vx, vy) in robots:
        currs.add((sx, sy))
    
    for y in range(SIZE[1]):
        for x in range(SIZE[0]):
            if (x, y) in currs:
                print("■", end="")
            else:
                print(" ", end="")
        print()
    input()

def main(lines):
    res = 0

    robots = []
    for line in lines:
        sx, sy = [int(x) for x in line.split()[0].split('=')[1].split(',')]
        vx, vy = [int(x) for x in line.split()[1].split('=')[1].split(',')]
        robots.append(((sx, sy), (vx, vy)))
        # print(robots[-1])
    
    for _ in range(10000):
        new_robots = []
        for (sx, sy), (vx, vy) in robots:
            sx += vx
            sy += vy
            sx %= SIZE[0]
            sy %= SIZE[1]
            new_robots.append(((sx, sy), (vx, vy)))
        robots = new_robots.copy()
        if ((_+1)%103) == 12:
            pr(robots, _)
    
    quad_size = SIZE[0]//2, SIZE[1]//2
    quads = dict()
    quads[((0, quad_size[0]), (0, quad_size[1]))] = 0
    quads[((SIZE[0] - quad_size[0], SIZE[0]), (0, quad_size[1]))] = 0
    quads[((SIZE[0] - quad_size[0], SIZE[0]), (SIZE[1] - quad_size[1], SIZE[1]))] = 0
    quads[((0, quad_size[0]), (SIZE[1] - quad_size[1], SIZE[1]))] = 0
    for (sx, sy), (vx, vy) in robots:
        for (xl, xh), (yl, yh) in quads:
            if xl <= sx < xh and yl <= sy < yh:
                quads[(xl, xh), (yl, yh)] += 1
    res = 1
    for x in quads.values():
        res *= x
    print(quads)
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
