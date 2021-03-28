import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')
'''
    DFS를 이용하여, 루트의 최단거리를 출력하여야 한다.
    왜 별로의 check배열을 두어 이를 놔두면, 오차가 발생하는지 의문.
'''
if __name__ == "__main__":
    n = 7

    dic = []
    dis = []
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    for i in range(n):
        arr = list(map(int, input().split()))  
        ch = [0]*n
        dis.append(ch)    
        dic.append(arr)

    start = [0,0]
    end = [6,6]
    queue = deque()
    queue.append(start)
    dic[0][0] = 1
    dis[6][6] = -1

    while queue:
        now = queue.popleft()

        if now[0] ==6 and now[1] == 6:
         
            break
        for i in move:
            x = i[0]+now[0]
            y = i[1]+now[1]

            if 0<=x<=6 and 0<=y<=6 and dic[x][y] == 0:
                dic[x][y] = 1
                queue.append([x,y])
                dis[x][y] = dis[now[0]][now[1]]+1

    print(dis[6][6])

        
        
        