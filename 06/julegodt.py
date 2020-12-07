ALVER = 127

godteri = [int(n) for n in open("godteri.txt").read().split(",")]
running_sum = 0
godteri_per_alv = 0
for g in godteri:
    running_sum += g
    if running_sum % ALVER == 0:
        godteri_per_alv += running_sum // ALVER
        running_sum = 0

print(godteri_per_alv)