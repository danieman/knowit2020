import re

def parse_line(line):
    rule = re.compile(r"(\w+) \[(.*)\]")
    line, names = re.match(rule, line).groups()
    return line, names.split(", ")

def count_line(line, names):
    total = 0
    for name in names:
        name = name.lower()
        if name_in_line(name, line):
            total += 1
            line = fix_line(line, name)
    return total

def name_in_line(name, line):
    for c in name:
        if c not in line:
            return False
        line = line[line.index(c) + 1:]
    return True

def fix_line(line, name):
    idx = []
    i = 0
    for c in name:
        i = line.find(c, i)
        idx.append(i)
    for i in reversed(idx):
        line = delete_by_idx(line, i)
    return line
    
def delete_by_idx(s, i):
    return s[:i] + s[i+1:]


lines = [line.strip() for line in open("input.txt").readlines()]
scores = [count_line(*parse_line(line)) for line in lines]
print(scores.index(max(scores)))