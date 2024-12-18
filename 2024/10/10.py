from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "10/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

ns = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def main(lines):
    res = 0
    zeroes = list()
    for ri, row in enumerate(lines):
        for ci, col in enumerate(row):
            if col == "0":
                zeroes.append((ri, ci))
    
    for zx, zy in zeroes:
        state = [{(zx, zy): 1}]
        for val in range(9):
            prev = state[-1]
            new_states = defaultdict(int)
            for (cx, cy) in prev:
                for dx, dy in ns:
                    nx, ny = cx+dx, cy+dy
                    if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]) and lines[nx][ny] == str(val+1):
                        new_states[(nx, ny)] += prev[(cx, cy)]
            state.append(new_states)
        print(sum(state[-1].values()))
        res += sum(state[-1].values())


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
