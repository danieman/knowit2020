visited = 0
stamina = 10
for c in open("rute.txt").read():
    if c == "1":
        stamina += 2
    visited += 1
    stamina -= 1
    if stamina == 0:
        break

print(visited)