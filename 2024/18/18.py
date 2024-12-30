from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "18/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

SIZE = 6
# SIZE = 70

LIMIT = 12
# LIMIT = 1024

ns = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def main(lines):
    res = 0
    LIMIT = 12

    def mini(l):
        blocked = set()
        for _ in range(LIMIT):
            v = tuple([int(x) for x in lines[_].split(',')])
            blocked.add(v)
        
        states = deque([(0, 0, 0)])
        seen = set([(0, 0)])
        while states:
            r, c, cost = states.popleft()
            if (r, c) == (SIZE, SIZE):
                return True
            for dr, dc in ns:
                nr, nc = r+dr, c+dc
                if 0 <= nr <= SIZE and 0 <= nc <= SIZE and (nr, nc) not in blocked:
                    if (nr, nc) not in seen:
                        states.append((nr, nc, cost+1))
                        seen.add((nr, nc))
            # print(states)
            # input()
        return False

    while True:
        res = mini(LIMIT)
        if not res:
            return lines[LIMIT]
        LIMIT += 1
        
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
