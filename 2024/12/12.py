from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "12/input.txt"

ns = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0

    seen = set()
    for ri, row in enumerate(lines):
        for ci, col in enumerate(row):
            if (ri, ci) not in seen:
                region = set([(ri, ci)])
                t = lines[ri][ci]
                permi = 0
                stack = [(ri, ci)]
                while stack:
                    cx, cy = stack.pop()
                    if (cx, cy) in seen:
                        continue
                    seen.add((cx, cy))
                    for dx, dy in ns:
                        nx, ny = cx+dx, cy+dy
                        if not (0 <= nx < len(lines) and 0 <= ny < len(lines[0])):
                            permi += 1
                        else:
                            if lines[nx][ny] == t:
                                stack.append((nx, ny))
                                region.add((nx, ny))
                            else:
                                permi += 1
                res += (len(region) * permi)
                print(t, len(region), permi)

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
