from copy import deepcopy

grid = [list(line.strip()) for line in open("elves.txt").readlines()]

xlimit = len(grid[0])
ylimit = len(grid)

days = 0
while True:
    days += 1
    old = deepcopy(grid)
    for y, row in enumerate(old):
        for x, col in enumerate(row):
            sick_neighbors = 0
            # Left
            if 0 <= x - 1 and old[y][x - 1] == "S":
                sick_neighbors += 1
            # Right
            if x + 1 < xlimit and old[y][x + 1] == "S":
                sick_neighbors += 1
            # Up
            if 0 <= y - 1 and old[y - 1][x] == "S":
                sick_neighbors += 1
            # Down
            if y + 1 < ylimit and old[y + 1][x] == "S":
                sick_neighbors += 1
            
            if sick_neighbors >= 2:
                grid[y][x] = "S"
    
    if old == grid:
        break

print(days)