import sys
from collections import deque

# sys.stdin = open("aaa.txt", "rt")

if __name__ == '__main__':
    N, M = map(int, input().split())

    dic = list(map(int, input().split()))
    dic.sort()
    cnt = 0

    for item in dic:
        cnt += 1
        if item == M:
            break

    print(cnt)
