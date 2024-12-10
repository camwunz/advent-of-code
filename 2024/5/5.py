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


def main(lines):
    res = 0
    key_before_val = defaultdict(list)

    for i, line in enumerate(lines):
        if line == "":
            break
        x, y = line.split("|")
        x = int(x)
        y = int(y)
        key_before_val[x].append(y)
    
    i += 1
    
    def is_valid(nums):
        nums = nums[::-1]
        seen = set()
        is_val = True
        for item in nums:
            if item in seen:
                return False
            else:
                seen = seen.union(set(key_before_val[item]))
        return True
            # print(nums)
    j = 0

    wrongs = []
    for rule in lines[i:]:
        nums = [int(x) for x in rule.split(",")]
        if not is_valid(nums):
            wrongs.append(nums)
    
    for nums in wrongs:
        nums = nums[::-1]
        while not is_valid(nums[::-1]):
            i = 0
            while i < len(nums):
                j = i + 1
                while j < len(nums):
                    if nums[j] in key_before_val[nums[i]]:
                        nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                i += 1
        res += nums[len(nums)//2]

    input()
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
