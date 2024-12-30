from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "19/input.txt"

ns = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines



def main(lines):
    res = 0
    towels = set(lines[0].split(', '))
    longest = max([len(x) for x in towels])
    cache = {}

    def can_make(towel):
        if towel == "":
            cache[towel] = 1
            return 1
        if towel in cache:
            return cache[towel]
        valid = 0
        i = 1
        while i <= min(longest+1, len(towel)):
            part = towel[:i]
            if part in towels:
                valid += can_make(towel[i:])
            i += 1
        cache[towel] = valid
        return valid
        
    goals = lines[2:]
    for goal in goals:
        res += can_make(goal)

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
