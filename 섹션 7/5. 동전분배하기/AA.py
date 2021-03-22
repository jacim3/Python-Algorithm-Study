import sys
# sys.stdin = open('input.txt','r')
# 시간초과 발생 -> 정적 함수 및 배열 최적화로 해결
def DFS(level):
    global mini
    if level == N:
        max_x = max(coin)
        min_n = min(coin)
        val = max_x - min_n
        if len(set(coin)) == 3:
            if val < mini: 
                mini = val
    else :
        for i in range(3):
            coin[i] += dic[level]
            DFS(level+1)
            coin[i] -= dic[level]

if __name__ == "__main__":
    N = int(input())
    mini = 9999
    dic = []
    coin = [0]*3
    ddd = [[],[],[]]
    for i in range(N):
        dic.append(int(input()))
    DFS(0)
    print(mini)
