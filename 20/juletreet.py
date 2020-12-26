from collections import defaultdict

def fire_mellomleder(name):
    for k, v in subs.items():
        if name in v:
            subs[k].add(name)
    to_be_fired.add(name)

lines = [line.strip().split("🎄") for line in open("elves.txt").readlines()]
hired = set([line[-1] for line in lines])
subs = defaultdict(set)

# Remove absent elves
for i in range(len(lines)):
    lines[i] = [e for e in lines[i] if e in hired]

# Add all elves to subordinate-tree
for line in lines:
    for i in range(len(line) - 1):
        subs[line[i]].add(line[i + 1])
    subs[line[-1]]

# Identify mellomledere
mellomledere = [elf for elf in subs if subs[elf]]
to_be_fired = set()

# Send all unnecessary mellomledere to firing
for k, v in subs.items():
    v = list(v)
    if len(v) == 1 and v[0] in mellomledere:
        fire_mellomleder(k)

# Fire all unnecessary mellomledere
for name in to_be_fired:
    del subs[name]

# Count arbeidere minus mellomledere
counts = [1 if v else 0 for v in subs.values()] 
print(counts.count(0) - counts.count(1))