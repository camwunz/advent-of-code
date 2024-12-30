from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
import networkx as nx
from aocd import submit, data

FILENAME = "23/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines

def check_strong(vals, adj_d):
    for v in vals:
        if (vals - adj_d[v] - {v}):
            return False
    return True

def main(lines):
    res = 0

    adj_d = defaultdict(set)
    alls = set()
    G = nx.Graph()
    e = []
    for line in lines:
        a, b = line.split('-')
        adj_d[a].add(b)
        adj_d[b].add(a)
        alls.add(a)
        alls.add(b)
        e.append((a, b))
    G = nx.Graph(e)
    n = 2
    while True:
        print(n, len(alls)//n)
        vals = nx.community.k_clique_communities(G, n)
        for option in vals:
            if check_strong(option, adj_d):
                return ",".join(sorted(option))
        n += 1

    
    # print(gots)
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
