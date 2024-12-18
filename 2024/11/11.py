from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "11/input.txt"
ns = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def main(lines):
    res = 0
    stones = [int(x) for x in lines[0].split()]
    stones = Counter(stones)
    for _ in range(75):
        new_stones = defaultdict(int)
        for stone, am in stones.items():
            if stone == 0:
                new_stones[1] += am
            elif len(str(stone)) % 2 == 0:
                a, b = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
                new_stones[int(a)] += am
                new_stones[int(b)] += am
            else:
                new_stones[(2024 * stone)] += am
        stones = new_stones.copy()
        print(_+1, sum(stones.values()))

    return len(stones)

if __name__ == "__main__":
    # test input
    print("TEST INPUT:")
    lines = get_input_from_file()
    # res = main(lines)
    # if res is not None:
    #     print(res)
    # print()
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
