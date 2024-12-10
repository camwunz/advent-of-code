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
    new_lines = lines.copy()
    lines = lines[0]
    stack = []
    i = 0
    t = 0
    stack = deque([])
    m = True

    for lines in new_lines:
        i = 0
        stack = deque([])
        nstack = deque([])
        while i < len(lines):
            stack.append(lines[i])
            nstack.append(lines[i])
            if len(stack) > 4:
                stack.popleft()
            if len(nstack) > 7:
                nstack.popleft()
            # print(list(nstack)[-4:])
            # input()
            if list(nstack)[-4:] == ['d', 'o', '(', ')']:
                m = True
            elif "".join(nstack) == "don't()":
                m = False
            # print(stack)
            # input()
            if list(stack) == ['m', 'u', 'l', '(']:
                new_stack = []
                i += 1
                while lines[i] in "0123456789,":
                    new_stack.append(lines[i])
                    nstack.append(lines[i])
                    if len(nstack) > 7:
                        nstack.popleft()
                    if list(nstack)[-4:] == ['d', 'o', '(', ')']:
                        m = True
                    elif "".join(nstack) == "don't()":
                        m = False
                    i += 1
                nstack.append(lines[i])
                if len(nstack) > 7:
                    nstack.popleft()
                if list(nstack)[-4:] == ['d', 'o', '(', ')']:
                    m = True
                elif "".join(nstack) == "don't()":
                    m = False
                if lines[i] == ")":
                    # print(new_stack)
                    # input()
                    try:
                        # print(new_stack)
                        x, y = [int(v) for v in "".join(new_stack).split(",")]
                        if m: t += x * y
                        # print(x, y)
                    except Exception:
                        pass
            i += 1
        # input()
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
