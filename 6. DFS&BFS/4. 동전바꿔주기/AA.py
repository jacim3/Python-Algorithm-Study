import sys
# sys.stdin = open('input.txt','r')
# 처음 생각했던 규칙이 맞았음. 2차원 배열에 담기
def DFS(level, sum):
    global count
    if sum < 0:
        return
    if level == K:
        if sum == 0:
            count = count+1
    else :
        for i in range(len(dic[level])+1):
            DFS(level+1, sum - i*dic[level][0])

if __name__ == "__main__":
    count = 0
    T = int(input())
    K = int(input())
    dic = []
    for i in range(K):
        arr = []
        P, N = map(int, input().split())
        for i in range(N):
            arr.append(P)
        dic.append(arr)
    DFS(0, T)
    print(count)