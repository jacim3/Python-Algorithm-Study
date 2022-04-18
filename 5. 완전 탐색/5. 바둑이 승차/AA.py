import sys
# sys.stdin = open('input.txt','r')

# 일정 수 이상 큰 값의 경우, Recursion 을 이용한 완전탐색을 이용할 경우,
# 시간초과가 발생 -> Cut Edge Tech 의 필요성.
# 각각의 노드에서 지나온 값들 = 판단한 값들 = tsum
# total - tsum = 앞으로 판단할 값
# hint : tsum + sum < max 의 경우, 이미 작은값이므로 판단할 필요 없이 return 하여 실행횟수를 줄일 수 있다.

MAX = 0;
def DFS(L, SUM, tSUM) :
    global MAX
    if SUM > C:
        return
    if (total-tSUM)+SUM < MAX :
        return
    if L == N:
     
        if MAX < SUM:
            MAX = SUM
            return
    else :
        # DFS 는 이러한 원리로 완전탐색을 수행한다.
        DFS(L+1, SUM+W[L], tSUM+W[L])
        DFS(L+1, SUM, tSUM+W[L])

if __name__ == "__main__":

    C, N = map(int, input().split())
    W = []
    for i in range(0, N):
        W.append(int(input()))
    total = sum(W)
    DFS(0, 0, 0)
    print(MAX)