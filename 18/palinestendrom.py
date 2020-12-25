def is_palinestendrom(word):
    if len(word) < 3 or word == word[::-1]:
        return False

    i = 0
    while i < len(word) // 2:
        if word[i] == word[-(i + 1)]:
            i += 1
            continue
        if word[i] + word[i + 1] != word[-(i + 2)] + word[-(i + 1)]:
            return False
        i += 2

    return True


words = [line.strip() for line in open("wordlist.txt").readlines()]
print(sum([is_palinestendrom(word) for word in words]))