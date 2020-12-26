from collections import defaultdict

def calculate_score(verse):
    score = 0
    prev, prev_bw = None, None
    rep = 1
    for word in verse:
        if prev is None:
            score += basescore[get_bw(word)]
        else:
            prev_bw = get_bw(prev)
            bw = get_bw(word)
            if bw == prev_bw:
                rep += 1
            else:
                rep = 1
            score += score_word(word, prev, rep)
        prev = word
    return score

def score_word(word, prev, rep=1):
    bp = basescore[get_bw(word)]
    vb = max(count_vowels(word) - count_vowels(prev), 0)
    if word.startswith("jule"):
        vb *= 2
    return (bp + vb) // rep

def count_vowels(word):
    vowels = "aeiouyæøå"
    return sum([word.count(v) for v in vowels])

def get_bw(word):
    return word[4:] if word.startswith("jule") else word


score = defaultdict(int)
basescore = {k: int(v) for k, v in [line.strip().split() for line in open("basewords.txt")]}
lines = [line.strip().split(": ") for line in open("rap_battle.txt")]

for artist, verse in lines:
    score[artist] += calculate_score(verse.split())
    
m = max(score, key=score.get)
print(f"{m},{score[m]}")