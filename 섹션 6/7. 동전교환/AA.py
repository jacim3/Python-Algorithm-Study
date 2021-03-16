import sys
# sys.stdin = open('input.txt','r')

def DFS(l, change) :
    global min
    # 핵심 base Case : 아마 보다 큰 갯수의 경우 시행할 필요가 없다. 
    if min < l :
        return
    if change < 0 :
        return;
    if change == 0:
       
        if min > l:
            min = l
    else :
        for i in range(0, N):
            DFS(l+1, change-DI[i])

if __name__ == "__main__":
    min = 9999999
    N = int(input())
    DI = list(map(int, input().split()))
    M  = int(input())
    # 정렬을 통하여, 시행횟수를 줄이기 위하여
    DI.sort(reverse=True)
    DFS(0, M)
    print(min)
