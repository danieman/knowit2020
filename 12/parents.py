from collections import defaultdict

tree = open("family.txt").read()
generations = defaultdict(int)

gen = 0
for i, char in enumerate(tree):
    if char == " " and tree[i - 1] != ")":
        generations[gen] += 1
    
    if char == "(":
        gen += 1
    
    if char == ")":
        if tree[i - 1].isalpha():
            generations[gen] += 1
        gen -= 1

print(max(generations.values()))