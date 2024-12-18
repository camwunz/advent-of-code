from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "15/input.txt"
ns = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

dirs = {'<': (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

def change_grid(grid):
    output = []
    for r in range(len(grid)):
        t = []
        for c in range(len(grid[0])):
            e = grid[r][c]
            if e == "#":
                t += ["#", "#"]
            elif e == "O":
                t += ["[", "]"]
            elif e == ".":
                t += [".", "."]
            elif e == "@":
                t += ["@", "."]
        output.append(t)
    return output

def move_up(grid, curr, dir, change = True):
    dr, dc = dirs[dir]
    in_bounds = lambda next_pos: 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])
    next_pos = (curr[0]+dr, curr[1]+dc)
    if not in_bounds(next_pos) or grid[next_pos[0]][next_pos[1]] == "#":
        return curr, False
    if grid[next_pos[0]][next_pos[1]] == ".":
        if change:
            grid[next_pos[0]][next_pos[1]] = grid[curr[0]][curr[1]]
            grid[curr[0]][curr[1]] = "."
        return next_pos, True
    
    # next_pos is a box
    posses = [next_pos]
    if grid[next_pos[0]][next_pos[1]] == "[":
        posses.append((next_pos[0], next_pos[1]+1))
    else:
        posses.append((next_pos[0], next_pos[1]-1))
    
    can_moves = []
    for pos in posses:
        _, possible = move_up(grid, pos, dir, change=False)
        can_moves.append(possible)
    if not all(can_moves):
        return curr, False
    for pos in posses:
        if change:
            move_up(grid, pos, dir, change=change)
    if change:
        grid[next_pos[0]][next_pos[1]] = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = "."
    return next_pos, True

def move(grid, curr, dir):
    if dirs[dir][1] == 0:
        new_pos, is_valid = move_up(grid, curr, dir)
        return new_pos
    dr, dc = dirs[dir]
    in_bounds = lambda next_pos: 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])
    next_pos = (curr[0]+dr, curr[1]+dc)
    if not in_bounds(next_pos) or grid[next_pos[0]][next_pos[1]] == "#":
        return curr
    if grid[next_pos[0]][next_pos[1]] == ".":
        grid[next_pos[0]][next_pos[1]] = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = "."
        return next_pos
    # next pos is a box
    move(grid, next_pos, dir)
    if grid[next_pos[0]][next_pos[1]] == ".":
        grid[next_pos[0]][next_pos[1]] = grid[curr[0]][curr[1]]
        grid[curr[0]][curr[1]] = "."
        return next_pos

    return curr

def calc_score(grid):
    s = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "[":
                s += (100 * r) + c
    return s

def main(lines):
    res = 0

    grid = []
    moves = []
    i = 0
    f = False
    while i < len(lines):
        if lines[i] == "":
            f = True
            i += 1
        if not f:
            grid.append(list(lines[i]))
        else:
            moves += list(lines[i])
        i += 1
    grid = change_grid(grid)
    curr = None
    for r in grid:
        print("".join(r))
    input()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # print(grid[r])
            if grid[r][c] == '@':
                curr = (r, c)

    debug = False

    for i, direction in enumerate(moves):
        print(i, len(moves))
        curr = move(grid, curr, direction)
        if debug:
            print("\n\n\nnew grid", direction)
            for r in grid:
                print("".join(r))
            input()
    
    return calc_score(grid)

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
