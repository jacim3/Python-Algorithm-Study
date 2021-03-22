import sys
# sys.stdin = open('input.txt','r')

# 풀이 1 - 2개의 가지로 뻗어가며,  모든 원소를 검색. 이 중 3개의 수를 더한 경우를 따로 추출
"""
def DFS(level, sum, cnt):
    global count
    if level == N :
        if cnt == K and sum % M == 0 and sum != 0:
            count = count+1
    else :
        DFS(level+1, sum+dic[level], cnt+1)
        DFS(level+1, sum, cnt)
        
   
if __name__ == "__main__":
    count = 0
    N, K = map(int, input().split())
    dic = list(map(int, input().split()))
    M = int(input())
    DFS(0, 0, 0)
    print(count)
"""

# 풀이2 - 별도의 시작점을 이용하여 가지 체크

def DFS(level, start, arr):
    global count
    if level == K :
        if sum(arr) % M == 0:  
            count = count+1
    else :
        for i in range(start, N):
            arr.append(dic[i])
            DFS(level+1, i+1, arr)
            arr.pop()
   
if __name__ == "__main__":
    count = 0
    N, K = map(int, input().split())
    dic = list(map(int, input().split()))
    M = int(input())
    DFS(0, 0, [])
    print(count)
