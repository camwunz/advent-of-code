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

def is_safe(nums):
    diffs = []
    for x, y in zip(nums, nums[1:]):
        diffs.append(y-x)
    if set(diffs) - {1, 2, 3} == set() or set(diffs) - {-1, -2, -3} == set():
        return True
    return False

def main(lines):
    t = 0
    for line in lines:
        nums = [int(x) for x in line.split()]
        if is_safe(nums):
            t += 1
            continue
        else:
            v = False
            for i in range(len(nums)):
                new_line = nums[:i] + nums[i+1:]
                # print(new_line)
                # input()
                if is_safe(new_line):
                    v = True
            if v:
                t += 1
                continue
    return t

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    res = main(lines)
    if res is not None:
        print(res)
    print()
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
