import sys, math
from collections import deque
# sys.stdin = open('input.txt','r')

'''
    풀이
    1. 중심점을 찾는다. (n//2, n//2)
    2. 중심점을 기준으로 시계방향으로 각 좌표를 탐색한다.
    3. 탐색 후 지정 범위를 벗어나게 될 경우 loof 를 탈줄한다.
'''
if __name__ == "__main__":
    n = int(input())
    dic = []
    check = [[0]*n for _ in range(n)]

    for i in range(n):
        arr = list(map(int, input().split()))
        dic.append(arr)
    
    center = [n//2, n//2]
    check[n//2][n//2] = 1
    total = dic[n//2][n//2]
    calc = [[-1,0],[0,1],[1,0],[0,-1]]
    edge = [[0, n//2],[n//2,n-1],[n-1, n//2],[n//2,0]]
    bfs = deque()
    bfs.append(center)
  
    while bfs:
        now = bfs.popleft()
        if edge[0] == now :
            break
        for next in calc:
            b = [now[0]+next[0], now[1]+next[1]]

            if check[b[0]][b[1]] == 0:
                check[b[0]][b[1]] = 1
                total += dic[b[0]][b[1]]
                bfs.append([b[0],b[1]])

    print(total)
           
            
 

