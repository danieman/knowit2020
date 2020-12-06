from collections import defaultdict

def parse(line):
    d = {}
    ingredients = line.strip().split(", ")
    for i in ingredients:
        name, amount = i.split(": ")
        d[name] = int(amount)
    return d


d = defaultdict(int)
for line in open("leveringsliste.txt").readlines():
    add = parse(line)
    for key, value in add.items():
        d[key] += value

print(min([d["melk"] // 3, d["mel"] // 3, d["sukker"] // 2, d["egg"]]))