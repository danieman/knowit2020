words = [line.strip() for line in open("wordlist.txt").readlines()]

horizontal = [line.strip() for line in open("matrix.txt").readlines()]
vertical = ["".join(col) for col in zip(*horizontal)]
diag1 = []
diag2 = []

size = len(horizontal)
idx = size - 1

for i in range(size):
    line = ""
    for j in range(i + 1):
        line += horizontal[i - j][j]
    diag1.append(line)

for i in range(idx):
    line = ""
    for j in range(idx - i):
        line += horizontal[idx - j][i + j + 1]
    diag1.append(line)

for i in range(size):
    line = ""
    for j in range(i + 1):
        line += horizontal[j][idx - i + j]
    diag2.append(line)

for i in range(idx):
    line = ""
    for j in range(idx - i):
        line += horizontal[i + j + 1][j]
    diag2.append(line)

missing = []
for word in words:
    rev = word[::-1]
    found = False
    for liste in [horizontal, vertical, diag1, diag2]:
        for line in liste:
            if word in line or rev in line:
                found = True
                break
        if found:
            break
    if found:
        print(f"✔️  {word}")
    else:
        print(f"❌ {word}")
        missing.append(word)

print()
print(",".join(sorted(missing)))