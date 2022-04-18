import math
import sys
from collections import deque

# sys.stdin = open("aaa.txt", "rt")

if __name__ == '__main__':
    K, N = map(int, input().split())

    dic = []
    for i in range(K):
        dic.append(int(input()))

    dic.sort(reverse=True)

    lt = 1
    rt = dic[0]
    MAX = 0
    while lt != rt:
        count = 0
        mid = (lt + rt) // 2

        for i in dic:
            count += i // mid
        if count >= N:
            MAX = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(MAX)