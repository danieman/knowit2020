from math import copysign

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
    
def update_times(pos):
    for place, coord in places.items():
        d = distance(*pos, *coord)
        if d == 0:
            continue
        elif d < 5:
            times[place] += 0.25
        elif d < 20:
            times[place] += 0.5
        elif d < 50:
            times[place] += 0.75
        else:
            times[place] += 1

def move(src, dst):
    x1, y1 = src
    x2, y2 = dst
    cur_pos = src
    xstep = int(copysign(1, x2 - x1))
    ystep = int(copysign(1, y2 - y1))
    for x in range(x1 + xstep, x2 + xstep, xstep):
        cur_pos[0] = x
        update_times(cur_pos)
    for y in range(y1 + ystep, y2 + ystep, ystep):
        cur_pos[1] = y
        update_times(cur_pos)
    return cur_pos
    
    
lines = [line.strip() for line in open("input.txt").readlines()]
places = {place: eval(coords) for place, coords in (line.split(": ") for line in lines[:50])}
times = {k: 0 for k in places.keys()}
trip = lines[50:]

current = [0, 0]
for place in trip:
    current = move(current, places[place])

print(max(times.values()) - min(times.values()))