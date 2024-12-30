from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "25/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0

    locks = []
    keys = []
    i = 0
    curr = []
    lines = lines + [""]
    while i < len(lines):
        print(i)
        if lines[i] == "":
            if set(curr[0]) == {"#"}:
                items = [1 for _ in range(len(curr[0]))]
                for row in curr[1:]:
                    for j, c in enumerate(row):
                        if c == '#':
                            items[j] += 1
                locks.append(items.copy())
            else:
                curr = curr[::-1]
                items = [1 for _ in range(len(curr[0]))]
                for row in curr[1:]:
                    for j, c in enumerate(row):
                        if c == '#':
                            items[j] += 1
                keys.append(items.copy())
            curr = []
        else:
            curr.append(lines[i])
        i += 1
    
    print(locks)
    print(keys)

    for lock in locks:
        for key in keys:
            can = True
            for a, b in zip(lock, key):
                if (a + b) > 7:
                    can = False
            if can:
                print(lock, key)
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
    input("waiting for input...")
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
