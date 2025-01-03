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

def split_as(a_movement):
    curr_pos = (2, 0)
    i = 0
    curr = []
    t = ""
    while i < len(a_movement):
        if a_movement[i] == "A" and curr_pos == (2, 0):
            t = t + "A"
            curr.append(t)
            t = ""
        else:
            t = t + a_movement[i]
            c = a_movement[i]
            if c == ">":
                curr_pos = (curr_pos[0]+1, curr_pos[1])
            elif c == "<":
                curr_pos = (curr_pos[0]-1, curr_pos[1])
            elif c == "^":
                curr_pos = (curr_pos[0], curr_pos[1]-1)
            elif c == "v":
                curr_pos = (curr_pos[0], curr_pos[1]+1)
        i += 1
    # print(a_movement, curr)
    # input()
    return curr

def main(lines):
    res = 0
    all_A_transforms = set(
        ['>>^A',
        ">>A",
        "vA",
        "^A",
        ">^A",
        ">vA",
        "<^A",
        "<vA",
        "A",
        "<A",
        ">A",
        "^<A",
        "v<A",
        "^>A",
        "v>A",
        "v<<A"]
    )

    # print(len(all_A_transforms))
    small_as_key = dict()
    for s in sorted(all_A_transforms):
        results = get_all([s], robot_grid)
        small_as_key[s] = results
    
    big_as_key = dict()
    for s in sorted(small_as_key):
        for k in small_as_key[s]:
            results = get_all([k], robot_grid)
            big_as_key[k] = results
    
    @cache
    def min_length(small_a, d):
        if d == 0:
            return len(small_a)

        possible_options = big_as_key[small_a]
        best = float('inf')
        for option in possible_options:
            small_as = split_as(option)
            total = 0
            for a in small_as:
                total += min_length(a, d-1)
            best = min(best, total)
        
        return best
    

    for line in lines:
        s1 = get_all([line], num_grid)
        s1 = get_all(s1, robot_grid)
        s1 = get_all(s1, robot_grid)
        # print(s1)
        num = int(line[:-1])
        best = float('inf')
        for option in s1:
            total = 0
            for small_a in split_as(option):
                total += min_length(small_a, 23)
            best = min(best, total)
        res += best * num
        # print(best, num)
        # input()
        
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
