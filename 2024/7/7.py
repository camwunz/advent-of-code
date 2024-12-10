from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "7/input.txt"

def get_input_from_file():
    try:
        with open(FILENAME) as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        with open("input.txt") as f:
            lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0
    for line in lines:
        val = int(line.split(":")[0])
        nums = [int(x) for x in line.split(":")[1].split()]
        states = set([nums[0]])
        for num in nums[1:]:
            new_states = set()
            for state in states:
                if state + num <= val:
                    new_states.add(state + num)
                if state * num <= val:
                    new_states.add(state * num)
                if int(str(state) + str(num)) <= val:
                    new_states.add(int(str(state) + str(num)))
            states = new_states.copy()
        if val in states:
            res += val
    return res

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    res = main(lines)
    if res is not None:
        print(res)
    print()
    # input("Waiting for input before running real...: ")
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
