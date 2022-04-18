import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')
'''

'''
def DFS(level, cursor, count):
    global maxi
    if level == n+1:
        if count > maxi :
            maxi = count
    else:
        for i in range(cursor+1, n+1):
            if one[level] == two[i]:
                DFS(level+1, i, count+1)

        DFS(level+1, cursor,count)

if __name__ == "__main__":
    n = int(input())
    maxi = 0
    one = []
    for i in range(n+1):
        one.append(i)
    two = list(map(int, input().split()))
    two = [0]+two
    DFS(1, 0, 0)
    print(maxi)
    