from string import ascii_lowercase as al

def find_nth(s, c, n):
    x = -1
    for i, b in enumerate(s):
        if b == c:
            x += 1
        if x == n:
            return i
    return -1

def remove_nth(s, c, n):
    i = find_nth(s, c, n)
    return s[:i].replace(c, "") + s[i] + s[i + 1:].replace(c, "")

s = open("text.txt").read()
for i, c in enumerate(al):
    s = remove_nth(s, c, i)
print(s)

