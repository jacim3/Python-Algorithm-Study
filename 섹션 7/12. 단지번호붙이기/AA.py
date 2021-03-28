import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')


'''
    풀이1. DFS 이나, 단지 마지막지점 탐색 이후 잡아내는 조건을 못 잡겠음
    -> 정석적인 풀이에서는 이것을 DFS 외부에 중첩 for문을 추가하여 해걸

def DFS(x,y):
    global cnt
    if x == n-1 and y == n-1 :
        return
    else :
        cnt2 = 0
        for i in move:
            next_x = i[0]+x
            next_y = i[1]+y
            
            if 0<=next_x<=n-1 and 0<=next_y<=n-1 and check[next_x][next_y] == 0:
                check[next_x][next_y] = 1
                if  board[next_x][next_y] == 1:
                    cnt+=1
                    
                DFS(next_x, next_y)
            else : cnt2 +=1
            if cnt !=0 and cnt2 ==4 :
                res.append(cnt)
                cnt = 0

if __name__ == "__main__":
    res = []
    n = int(input())
    cnt = 0
    board = [ list(map(int, input())) for _ in range(n)]
    check = [ [0]*n for _ in range(n)]
    result = [ [0]*n for _ in range(n)]
    #for i in board:
    #    print(i)
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    DFS(0,-1)
    print(res)        
'''
def DFS(x, y):
    global cnt
    cnt +=1
    board[x][y] = 0
    for i in move:
        xx = i[0]+x
        yy = i[1]+y
        if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy] == 1:
            board[xx][yy] = 0
            
            DFS(xx,yy)

if __name__ == "__main__":
    n = int(input())
    board = [ list(map(int, input())) for _ in range(n)]
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    cnt = 0
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] ==1 :
                cnt = 0    
                DFS(i,j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for i in res:
        print(i)