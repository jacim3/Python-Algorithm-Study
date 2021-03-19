import sys
# sys.stdin = open('input.txt','r')
# 풀이1 - 몇몇 test case 에서 1만큼 오차 발생 -> fix. 증감중 0 이 발생하였을때 이를 제거해 주어야 함. 유효 범위 = 1<= x <= S
# DFS 를 2번 사용하여 풀이. but 풀이2에서 1회의 DFS로도 해결이 가능. 결국 status chart를 어떻게 작성하는지가 중요!!!
def DFS(level, arr):
    if level == K:
        if len(arr) != 0 :
            DFS2(0, arr, 0)
    else :
        arr.append(dic[level])
        DFS(level+1, arr)
        arr.pop()
        DFS(level+1,arr)
            
def DFS2(level, arr, val):
    if level == len(arr) :
        if val > 0:
            total.append(abs(val))
    else :
        DFS2(level+1, arr, val+arr[level])
        DFS2(level+1, arr, val-arr[level])

    
if __name__ == "__main__":
    K = int(input())
    dic = list(map(int, input().split()))
    S = sum(dic)
    total = []
    DFS(0, [])
    a_set = set(total)
    # print(a_set)
    print(S - len(a_set))
"""
def DFS(level, val) :
    if level == K:
        if val >0 :
            total.append(abs(val))
    else :
        DFS(level+1, val+dic[level])
        DFS(level+1, val-dic[level])
        DFS(level+1, val)

if __name__ == "__main__":
    K = int(input())
    dic = list(map(int, input().split()))
    S = sum(dic)
    total = []
    DFS(0, 0)
    s_total = set(total)

    print(S-len(s_total))
"""