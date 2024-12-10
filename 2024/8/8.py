from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "8/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0
    locs = defaultdict(list)
    for ri, row in enumerate(lines):
        for ci, col in enumerate(row):
            if col != ".":
                locs[col].append((ri, ci))

    antis = set()
    for ty in locs:
        for a, b in combinations(locs[ty], 2):
            # print(a, b)
            antis.add(a)
            antis.add(b)
            dx = (b[0] - a[0])
            dy = (b[1] - a[1])
            prev = (a[0] - dx, a[1] - dy)
            nex = (b[0] + dx, b[1] + dy)
            while 0 <= prev[0] < len(lines) and 0 <= prev[1] < len(lines[0]):
                # print(prev)
                antis.add(prev)
                prev = (prev[0] - dx, prev[1] - dy)
            while 0 <= nex[0] < len(lines) and 0 <= nex[1] < len(lines[0]):
                # print(nex)
                antis.add(nex)  
                nex = (nex[0] + dx, nex[1] + dy)
    print(list(sorted(antis)))
    return len(antis)

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
            submit(res)
        else:
            print("\x1B[3mNot submitting...\x1B[0m")
    else:
        print("\x1B[3mNo answer returned, not submitting\x1B[0m")
