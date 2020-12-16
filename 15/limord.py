wordlist = set([line.strip() for line in open("wordlist.txt").readlines()])
pairs = [line.strip().split(", ") for line in open("riddles.txt").readlines()]
limord = set()

for w1, w2 in pairs:
    for word in wordlist:
        if w1 + word in wordlist and word + w2 in wordlist:
            limord.add(word)

print(sum([len(s) for s in limord]))