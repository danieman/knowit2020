with open("numbers.txt", "r") as f:
    numbers = sorted([int(n) for n in f.read().split(",")])

for i, n in enumerate(numbers):
    if n != i + 1:
        print(i+1)
        break