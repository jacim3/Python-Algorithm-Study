import sys
# sys.stdin = open('input.txt','r')

def DFS(level, sum):
    global maxi
    if level > N :
        return
    if level == N :
        if maxi < sum :
            maxi = sum
    else :
            DFS(level+dic[level][0], sum+dic[level][1])
            DFS(level+1, sum)
          
    
if __name__ == "__main__":
    N = int(input())
    maxi = 0
    dic = [[0]*2 for _ in range(N)]

    for i in range(N):
        a,b = map(int, input().split())
        dic[i][0] = a
        dic[i][1] = b
    DFS(0, 0)
    print(maxi)