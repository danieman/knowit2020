def check_tree(a, b):
    return all([line[a + 1:b] == line[a + 1:b][::-1] for line in forest])

forest = [line.strip("\n") for line in open("forest.txt").readlines()]
spaces = [-1]
for i in range(len(forest[0])):
    if all([line[i] == " " for line in forest]):
        spaces.append(i)

print(sum([1 for i in range(0, len(spaces) - 1, 2) if check_tree(spaces[i], spaces[i + 1])]))