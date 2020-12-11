from collections import defaultdict

leker = [line.strip().split(",") for line in open("leker.txt").readlines()]
alver = defaultdict(int)
for lek in leker:
    max_poeng = len(lek)
    for idx, alv in enumerate(lek, start=1):
        alver[alv] += (max_poeng - idx)
        
k, v = max(alver.items(), key=lambda x: x[1])
print(f"{k}-{v}")