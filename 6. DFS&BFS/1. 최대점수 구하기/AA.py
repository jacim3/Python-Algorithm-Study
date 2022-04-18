import sys
# sys.stdin = open('input.txt','r')

def DFS(level, sum, time):
    global maxi
    if time > M :
        return
    if level == N :
        if maxi < sum :
            maxi = sum
    else :
            DFS(level+1, sum+dic[level][0], time+dic[level][1])
            DFS(level+1, sum, time)
          
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    maxi = 0

    dic = [[0]*2 for _ in range(N)]
    check = [0]*N
    for i in range(N):
        a,b = map(int, input().split())
        dic[i][0] = a
        dic[i][1] = b
    DFS(0, 0, 0)
    print(maxi)
        