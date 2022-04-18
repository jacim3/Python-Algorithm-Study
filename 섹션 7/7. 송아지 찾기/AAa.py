import sys

# sys.stdin = open("aaa.txt", "rt")


def rec(level, loc):
    global E, MIN
    if level != 0 and loc < 1:
        return
    if loc == E:
        if MIN > level :
            MIN = level

    if loc < E:
        rec(level + 1, loc + 1)
        rec(level + 1, loc + 5)
    elif loc > E:
        rec(level + 1, loc + -1)


if __name__ == '__main__':
    command = [1, -1, 5]
    MIN = 1000
    MAX = 10000

    S, E = map(int, input().split())
    rec(0, S)
    print(MIN)
