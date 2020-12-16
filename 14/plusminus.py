LENGTH = 1_800_813

def isprime(n):
    if n in [0, 1]:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    ctr = 3
    s = n ** 0.5
    while ctr <= s:
        if n % ctr == 0:
            return False
        ctr += 2
    return True

seen = {0, 1}
numbers = [0, 1]

n = 2
while len(numbers) < LENGTH:
    num = numbers[-2]
    if num - n > 0 and num - n not in seen:
        numbers.append(num - n)
        seen.add(num - n)
    else:
        numbers.append(num + n)
        seen.add(num + n)
    n += 1
print("hei")
print(sum([isprime(n) for n in seen]))