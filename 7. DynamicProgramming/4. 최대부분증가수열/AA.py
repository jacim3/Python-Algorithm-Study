import sys, math
from collections import deque
sys.stdin = open('input.txt','rt')
'''
   가장 작은 단위로 분할하여 해결할 것! 
'''

'''
    풀이1. Dynamic programming
    
'''

                
              
if __name__ == "__main__":
    n = int(input())
    dic = list(map(int, input().split()))
    memo = [0] * n
    memo[0] = 1
    memo[1] = 1
    cursor = 0
    
    for i in range(2, n):
        # 항목이 바뀔때 마다 값은 초기화 해 주어야 한다.
        maxi = 0
        for j in range(i):
            if dic[i] > dic[j] :
                if maxi < memo[j] :
                    maxi = memo[j]

        memo[i] = maxi+1
    a = max(memo)
    print(a)

        
'''
    풀이2. DFS
    조건문을 통한 arr 배열에 재귀호출을 이용
    각각의 end point에 대한 반복문을 통하여 여러개의 재귀문을 실행
    재귀문들은 각각의 end point에 따라 서로 다른 결과를 출력..
    현재 코드가 불완전함
'''
"""
def DFS(level, arr, end):
    global maxi
    if level == end:
        print(arr)
        if maxi < len(arr):
            maxi = len(arr) 
    else :
        if dic[end] > dic[level]:
            if len(arr) == 0 or arr[len(arr)-1] < dic[level]:
                arr.append(dic[level])
        DFS(level+1, arr, end)

if __name__ == "__main__":
    n = int(input())
    dic = list(map(int, input().split()))

    maxi = 0
    for i in range(n-1, -1, -1):
        DFS(0, [], i)
    print(maxi+1)
"""