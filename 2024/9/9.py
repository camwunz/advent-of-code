from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "9/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0
    nums = list(lines[0])
    # even = data
    # odd = free
    count = 0
    data = []
    for i, size in enumerate(nums):
        size = int(size)
        if i % 2 == 0:
            data.append([count] * size)
            count += 1
        else:
            data.append(["."] * size)
    # print(data)
    data = sum(data, [])
    left = 0
    right = len(data) - 1

    while True:
        print(right, len(data))
        while right == ".":
            right -= 1
        rightsize = 0
        tright = right
        while data[tright] == data[right]:
            rightsize += 1
            tright -= 1
        leftsize = 0
        left = 0

        while True:
            while data[left] != ".":
                left += 1
            leftsize = 0
            tleft = left
            if left > right:
                break
            while data[tleft] == ".":
                tleft += 1
                leftsize += 1
            if leftsize >= rightsize:
                break
            left += leftsize
            if left > right:
                break
        if leftsize >= rightsize:
            for _ in range(rightsize):
                data[left] = data[right]
                data[right] = "."
                left += 1
                right -= 1
        else:
            right -= rightsize
        if right <= 0:
            break
        # print(data)
            
    t = 0
    for i, j in enumerate(data):
        if j == ".":
            continue
        t += i * int(j)
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
