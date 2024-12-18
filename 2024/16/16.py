from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "16/input.txt"
ns = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    dp = defaultdict(lambda: float('inf'))
    states = deque([])
    end = None
    start = None
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "S":
                states.append((r, c, 0, 0))
                start = r, c
            elif lines[r][c] == "E":
                end = (r, c)

    dp[(*start, 0)] = 0
    while states:
        cr, cc, dir_index, score = states.popleft()
        dx, dy = dirs[dir_index]
        nr, nc = cr+dx, cc+dy
        if lines[nr][nc] != "#":
            if dp[(nr, nc, dir_index)] > score+1:
                dp[(nr, nc, dir_index)] = score+1
                states.append((nr, nc, dir_index, score+1))
        for _ in range(4):
            dir_index += 1
            dir_index %= 4
            if dp[(cr, cc, dir_index)] > score+1000:
                dp[(cr, cc, dir_index)] = score+1000
                states.append((cr, cc, dir_index, score+1000))
        # print(states)
        # input()
    
    # go backwards part


    best = float('inf')
    last_dir = None
    for d in range(4):
        cost = dp[(*end, d)]
        if cost < best:
            last_dir = d
            best = cost
    # print(last_dir)
    
    tiles = set([end])
    states = deque([(*end, last_dir)])
    while states:
        cr, cc, dir_index = states.popleft()
        dx, dy = dirs[dir_index]
        nr, nc = cr-dx, cc-dy
        if dp[(nr, nc, dir_index)] == dp[(cr, cc, dir_index)]-1:
            tiles.add((nr, nc))
            states.append((nr, nc, dir_index))
        base_dir = dir_index
        for _ in range(4):
            dir_index += 1
            dir_index %= 4
            if dp[(cr, cc, dir_index)] == dp[(cr, cc, base_dir)]-1000:
                tiles.add((cr, cc))
                states.append((cr, cc, dir_index))


    return len(tiles)

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
