import sys
from collections import deque


#sys.stdin = open("aaa.txt", "rt")

if __name__ == '__main__':
    N = int(input())
    SET = []
    MAX = 0
    for i in range(N):
        s, e = map(int, input().split())
        SET.append([s, e])

    # 2차원 배열을 특정값을 기준으로 정렬하기!!!
    SET.sort(key=lambda x: (x[1]))

    et = 0
    for s, e in SET:
        if s >= et:
            et = e
            MAX += 1

    print(MAX)
