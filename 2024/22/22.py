from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "22/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines


def transform(num):
    num = num ^ (num * 64)
    num %= 16777216
    num = num ^ (num // 32)
    num %= 16777216
    num = num ^ (num * 2048)
    num %= 16777216
    return num

def main(lines):
    res = 0

    loops = 2000
    possible_seqs = set()
    costs = []
    for line in lines:
        num = int(line)
        local_seens = defaultdict(int)
        cu_ds = deque([])
        for _ in range(loops):
            next = transform(num)
            cu_ds.append((next % 10) - (num % 10))
            if len(cu_ds) > 4:
                cu_ds.popleft()
            if len(cu_ds) == 4:
                options = tuple(cu_ds)
                possible_seqs.add(options)
                if options not in local_seens:
                    local_seens[options] = next % 10
            num = next

        costs.append(local_seens)

    best = float('-inf')
    print(len(possible_seqs))
    for i, seq in enumerate(possible_seqs):
        print(i, len(possible_seqs))
        cost_for_seq = 0
        for local_seen in costs:
            cost_for_seq += local_seen[seq]

        best = max(best, cost_for_seq)

    return best

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
