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

def get_sides(sides):
    sides_am = 0
    for dx, dy in sides:
        groupings = sides[(dx, dy)]
        seen = set()
        check_move = None
        if dy == 0:
            check_move = [(0, 1), (0, -1)]
        else:
            check_move = [(1, 0), (-1, 0)]
        for start_group in groupings:
            if start_group in seen:
                continue
            local_seen = set([start_group])
            seen.add(start_group)
            while True:
                to_add = set()
                for match_group in groupings:
                    mgx, mgy = match_group
                    if match_group in seen:
                        continue
                    for pcx, pcy in local_seen:
                        if (mgx - pcx, mgy - pcy) in check_move:
                            to_add.add((mgx, mgy))
                            seen.add((mgx, mgy))
                if not to_add:
                    break
                local_seen |= to_add
            sides_am += 1
            print("side ", list(sorted(local_seen)))
    return sides_am

def main(lines):
    res = 0

    seen = set()
    for ri, row in enumerate(lines):
        for ci, col in enumerate(row):
            if (ri, ci) not in seen:
                region = set([(ri, ci)])
                sides = defaultdict(list)
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
                            sides[(dx, dy)].append((nx, ny))
                        else:
                            if lines[nx][ny] == t:
                                stack.append((nx, ny))
                                region.add((nx, ny))
                            else:
                                sides[(dx, dy)].append((nx, ny))
                

                sides_am = get_sides(sides)
                res += sides_am * len(region)
                
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
