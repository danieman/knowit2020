from copy import deepcopy

def sick_neighbours(coords, grid):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    visible = 0
    for x, y in directions:
        xpos, ypos = coords
        if 0 <= xpos + x < xlimit and 0 <= ypos + y < ylimit:
            if grid[ypos + y][xpos + x] == "S":
                visible += 1
    return visible

grid = [list(line.strip()) for line in open("elves.txt").readlines()]
xlimit = len(grid[0])
ylimit = len(grid)

days = 0
while True:
    days += 1
    old = deepcopy(grid)
    for y, row in enumerate(old):
        for x, col in enumerate(row):
            sick = sick_neighbours([x, y], old)
            if sick >= 2:
                grid[y][x] = "S"
    if old == grid:
        break

print(days)