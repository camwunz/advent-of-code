from collections import *
ins = '23/input2.txt'
out = 'output.txt'
f = open(out, 'w')
lines = open(ins).read().splitlines()
adj_d = defaultdict(set)
alls = set()
js = []
for line in lines:
    a, b = line.split('-')
    js.append(f"{a} {b}")
    adj_d[a].add(b)
    adj_d[b].add(a)
    alls.add(a)
    alls.add(b)

for a in sorted(alls):
    f.write(f'{a}\n')
for j in js:
    f.write(f'{j}\n')
