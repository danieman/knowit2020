def PolygonArea(corners):
    # https://stackoverflow.com/a/24468019
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

corners = [(0, 0)]
pos = [0, 0]
path = open("rute.txt").read().strip()
for d in path:
    if d == "H":
        pos[0] += 1
    elif d == "V":
        pos[0] -= 1
    elif d == "O":
        pos[1] += 1
    elif d == "N":
        pos[1] -= 1
    else:
        print(d)
    corners.append(tuple(pos))

print(PolygonArea(corners))