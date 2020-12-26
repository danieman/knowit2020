from collections import defaultdict, Counter
import re


def parse_line(line):
    rule = re.compile(r"(\d+) (\d+) (.*)")
    a, b, c = re.match(rule, line).groups()
    return (int(a), int(b), parse_list(c))


def parse_list(s):
    return s[1:-1].split(", ")


def rotate(players, hops):
    while hops > 0:
        players = [players[-1]] + players[:-1]
        hops -= 1
    return players


def play_game(rule, hops, players):
    i = 0
    while len(players) > 1:
        players = rotate(players, hops)
        if rule == 1:
            del players[0]
        elif rule == 2:
            del players[i]
            i = (i + 1) % len(players)
        elif rule == 3:
            m = len(players) // 2
            if len(players) % 2:
                del players[m]
            elif len(players) == 2:
                del players[0]
            else:
                del players[m:m + 2]
        elif rule == 4:
            del players[-1]
    #print(f"Winner: {players[0]}")
    return players[0]


lines = [parse_line(line.strip()) for line in open("input.txt").readlines()]
winners = [play_game(*line) for line in lines]

c = Counter(winners)
print(c.most_common(3))