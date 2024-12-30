from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "21/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

num_grid = {"7": (0, 0), "8": (1, 0), "9": (2, 0),
            "4": (0, 1), "5": (1, 1), "6": (2, 1),
            "1": (0, 2), "2": (1, 2), "3": (2, 2),
            "": (0, 3), "0": (1, 3), "A": (2, 3)}

robot_grid = {"": (0, 0), "^": (1, 0), "A": (2, 0),
              "<": (0, 1), "v": (1, 1), ">": (2, 1)}

def min_moves(start, end, grid):
    start_coord = grid[start]
    end_coord = grid[end]
    moves = []
    options = {'up': True, 'across': True}
    if len(grid) == 6:
        if start_coord[0] == 0 and end_coord[1] == 0:
            options['up'] = False
        if start_coord[1] == 0 and end_coord[0] == 0:
            options['across'] = False
    else:
        if start_coord[0] == 0 and end_coord[1] == 3:
            options['up'] = False
        if start_coord[1] == 3 and end_coord[0] == 0:
            options['across'] = False

    move_options = []
    options = [k for k in options if options[k]]
    for go_first in options:
        moves = []
        if go_first == "up":
            if start_coord[1] > end_coord[1]:
                for u in range(start_coord[1]-end_coord[1]):
                    moves.append("^")
            elif start_coord[1] < end_coord[1]:
                for u in range(end_coord[1]-start_coord[1]):
                    moves.append("v")
        
            # have to go to the side
            if start_coord[0] < end_coord[0]:
                # right
                for u in range(end_coord[0] - start_coord[0]):
                    moves.append(">")
            elif start_coord[0] > end_coord[0]:
                # left
                for u in range(start_coord[0] - end_coord[0]):
                    moves.append("<")
        else:
            # have to go to the side
            if start_coord[0] < end_coord[0]:
                # right
                for u in range(end_coord[0] - start_coord[0]):
                    moves.append(">")
            elif start_coord[0] > end_coord[0]:
                # left
                for u in range(start_coord[0] - end_coord[0]):
                    moves.append("<")
            
            if start_coord[1] > end_coord[1]:
                for u in range(start_coord[1]-end_coord[1]):
                    moves.append("^")
            elif start_coord[1] < end_coord[1]:
                for u in range(end_coord[1]-start_coord[1]):
                    moves.append("v")

        moves.append("A")
        move_options.append(moves.copy())
    return move_options

def get_all(lines, grid):
    output = set()
    for line in lines:
        line = ["A"] + list(line)
        pairs = pairwise(line)
        options = set([""])
        for s, e in pairs:
            total_results = min_moves(s, e, grid)
            new_options = set()
            for o in options:
                for r in total_results:
                    new_options.add(o + "".join(r))
            options = new_options.copy()
        output = output.union(options)
    return output
    
def main(lines):
    res = 0
    all_A_transforms = set()
    for line in lines:
        
        options = get_all([line], num_grid)
        for _ in range(3):
            min_len = min([len(x) for x in options])
            options = [x for x in options if len(x) == min_len]
            options = get_all(options, robot_grid)
            print(_, min_len)
        best = min(options, key=len)
        x = len(best)
        num = int(line[:-1])
        res += num * x
        print(num, x)

        
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
