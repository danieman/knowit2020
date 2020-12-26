from collections import defaultdict

def generateFactors(n):
    factors = defaultdict(list) 
    i = 1
    while (i * i < n):
        for j in range(i, n, i):
            factors[j].append(i)
            factors[j].append(j // i)
        i += 1
    return factors

def is_square(n):
    return n ** 0.5 == int(n ** 0.5)

factors = generateFactors(10 ** 6)
total = 0
for n in range(1, 10 ** 6):
    sum_d = sum(set(factors[n]))
    if sum_d > 2*n and is_square(abs(sum_d - 2 * n)):
        total += 1

print(total)