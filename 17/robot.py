def does_robot_fit(x, y, max_w, max_h, m, r):
    """Takes in x, y, map and relative robot coordinates"""
    actual = {(x + xpos, y + ypos) for xpos, ypos in r}
    for xpos, ypos in actual:
        if xpos < 0 or xpos >= max_w or ypos < 0 or ypos >= max_h:
            return False
        if m[ypos][xpos] == "x":
            return False
    return True

def get_cleaned_points(x, y, b):
    """Takes in x, y and relative brush coordinates"""
    actual = {(x + xpos, y + ypos) for xpos, ypos in b}
    return actual

# Set relative brush coordinates
brushes = set()
for xpos in range(-4, 5):
    if xpos not in [-1, 0, 1]:
        brushes.add((xpos, -4))
        brushes.add((xpos, 4))
for xpos in range(-4, 5):
    for ypos in range(-3, 4):
        if not (xpos in [-4, 4] and ypos in [-1, 0, 1]):
            brushes.add((xpos, ypos))

# Set relative robot coordinates
robot = set()
for xpos in range(-1, 2):
    robot.add((xpos, -3))
    robot.add((xpos, 3))
for xpos in range(-2, 3):
    robot.add((xpos, -2))
    robot.add((xpos, 2))
for xpos in range(-3, 4):
    for ypos in range(-1, 2):
        robot.add((xpos, ypos))

# Read map
kart = [list(line.strip("\n")) for line in open("kart.txt").readlines()]
# Read test map
#kart = [list(line.strip()) for line in open("test.txt").readlines()]

# Loop through map and clean it
rows = len(kart)
cols = len(kart[0])
for y in range(rows):
    print(f"\rDone searching row {y + 1} of {rows} ...", end="")
    for x in range(cols):
        if not does_robot_fit(x, y, cols, rows, kart, robot):
            continue
        clean = get_cleaned_points(x, y, brushes)
        for xpos, ypos in clean:
            if xpos < 0 or xpos >= cols or ypos < 0 or ypos >= rows:
                continue
            if kart[ypos][xpos] == " ":
                kart[ypos][xpos] = "."

print()  
print(sum([l.count(" ") for l in kart]))

# Write cleaned map to file
with open("cleaned_kart.txt", "w") as f:
    for line in kart:
        f.write("".join(line) + "\n")