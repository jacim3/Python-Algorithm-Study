import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')
'''
    모든 경우의 수를 구하는 문제이므로 DFS를 이용!!!
    
    board의 중복을 체크하는 부분에서 = 이 아닌 == 를 사용하여 recursion 오류가 발생 -> 오타
'''
def DFS(level, now):
    global cnt
    if end == now:
        cnt=cnt+1
    else:

        for i in move :
        
            x = now[0]+i[0]
            y = now[1]+i[1]
            if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
                
                board[x][y] = 1
                DFS(level+1,[x,y])
                board[x][y] = 0


if __name__ == "__main__":
    n = 7

    board = []
    move = [[-1,0],[0,1],[1,0],[0,-1]]
    for i in range(n):
        arr = list(map(int, input().split()))   
        board.append(arr)

    start = [0,0]
    end = [6,6]
    board[0][0] = 1
    cnt = 0
    DFS(0, [0,0])
    print(cnt)

        
        
        