from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

ns = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
combs = [
    [
        "M.S",
        ".A.",
        "M.S",
    ],
    [
        "S.M",
        ".A.",
        "S.M",
    ],
    [
        "M.M",
        ".A.",
        "S.S",
    ],
    [
        "S.S",
        ".A.",
        "M.M",
    ]
]
def main(lines):
    ts = 0
    for start_row in range(len(lines)-2):
        for start_col in range(len(lines[0])-2):
            block = [
                lines[start_row][start_col:start_col+3],
                lines[start_row+1][start_col:start_col+3],
                lines[start_row+2][start_col:start_col+3],
            ]
            v = False
            for item in combs:
                tv = True
                for b, c in zip(block, item):
                    # print(b, c)
                    for bchar, cchar in zip(b, c):
                        if bchar == cchar or cchar == ".":
                            continue
                        else:
                            tv = False
                if tv:
                    ts += 1
            # if v: 
            #     ts += 1
            # print(start_row, start_col)
    # input()
    return ts

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    res = main(lines)
    if res is not None:
        print(res)
    print()
    # real input
    print("REAL INPUT:")
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
