import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')

def DFS(start,x, y):
    global cnt
    if start == maxi:
        cnt +=1
    else :
        
        for i in move:
            xx = i[0]+x
            yy = i[1]+y
            if 0<=xx<=n-1 and 0<=yy<=n-1 and start < board[xx][yy] :
                next = board[xx][yy]
                board[xx][yy] = 0
                DFS(next, xx, yy)
                board[xx][yy] = next


if __name__ == "__main__":

    n = int(input())
    board = []
    mini = 9999
    maxi = 0
    cnt = 0
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    sx = 0
    xy = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        if mini > min(tmp):
            mini =  min(tmp)
            sx = i
        if maxi < max(tmp):
            maxi = max(tmp)

    for i in range(n):
        if mini == board[sx][i]:
            sy = i
    board[sx][sy] = 0
    DFS(mini,sx, sy)
    print(cnt)

        
        
        