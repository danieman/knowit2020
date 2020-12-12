from string import ascii_lowercase as al
from itertools import zip_longest

PW = "eamqia"

def generate_passwords(hint):
    hints = [hint]
    while len(hint) > 1:
        hint = next_step(hint)
        hints.append(hint)

    return ["".join(l) for l in zip_longest(*hints, fillvalue="")]

def next_step(prev):
    w1 = prev[1:]
    w2 = ""
    for c in w1:
        w2 += inc(c)
    w3 = ""
    for i, c in enumerate(w2):
        w3 += plus(prev[i], w2[i])
    return w3

def inc(c):
    return al[(al.index(c) + 1) % len(al)]

def plus(c1, c2):
    return al[(al.index(c1) + al.index(c2)) % len(al)]

def isvalid(pw, pwlist):
    for p in pwlist:
        if pw in p:
            return True
    return False


candidates = [line.strip() for line in open("hint.txt").readlines()]

for word in candidates:
    pws = generate_passwords(word)
    if isvalid(PW, pws):
        print(word)
        break