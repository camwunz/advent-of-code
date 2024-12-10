from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "6/input.txt"

def get_input_from_file():
    try:
        with open(FILENAME) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        with open("input.txt") as f:
            lines = f.read().splitlines()
    return lines

def main2(lines):
    res = 0
    curr = (0, 0)
    for ri, row in enumerate(lines):
        for ci, e in enumerate(row):
            if e == "^":
                curr = (ri, ci)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set([(curr, 0)])
    curr_dir = 0
    while True:
        nx, ny = curr[0] + dirs[curr_dir][0], curr[1] + dirs[curr_dir][1]
        if not (0 <= nx < len(lines) and 0 <= ny < len(lines[0])):
            break
        if lines[nx][ny] == "#":
            curr_dir += 1
            curr_dir %= 4
        else:
            curr = (nx, ny)
            if (curr, curr_dir) in seen:
                return False
            seen.add((curr, curr_dir))
    # input()
    return True

def main(lines):
    t = 0
    for ri, row in enumerate(lines):
        for ci, col in enumerate(row):
            print(ri, ci)
            if lines[ri][ci] == ".":
                base = [list(x) for x in lines.copy()]
                base[ri][ci] = "#"
                # for x in base:
                #     print(x)
                # input()
                if not main2(base):
                    t += 1
    return t

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    res = main(lines)
    if res is not None:
        print(res)
    print()
    # real input
    print("REAL INPUT")
    res = main(data.splitlines())
    if res is not None:
        print(res)
        to_submit = input("Would you like to submit? (y/n): ").strip().lower()
        if to_submit == "y":
            print("\x1B[3mSubmitting...\x1B[0m")
            submit(res)
        else:
            print("\x1B[3mNot submitting...\x1B[0m")
    else:
        print("\x1B[3mNo answer returned, not submitting\x1B[0m")
