from collections import deque

def treat_new(queue):
    idx = 0
    while len(queue[idx]) == 0:
        idx += 1
    return queue[idx].popleft()

def main():
    visitors = [line.strip() for line in open("input.txt").readlines()]
    queue = [deque() for _ in range(5)]
    treated = 0

    for line in visitors:
        if line == "---":
            client = treat_new(queue)
            if client == "Claus":
                print(treated)
                return
            treated += 1
        else:
            name, idx = line.split(",")
            queue[int(idx) - 1].append(name)

    while client != "Claus":
        client = treat_new(queue)
        treated += 1

    print(treated - 1)

if __name__ == "__main__":
    main()