import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')

'''
    Dynamic programming
'''
'''
    1. Bottom-Up 방식 : 점화식
    풀이가 불가능할 정도로 규모가 큰 문제를 우리가 직관적으로 알아볼 수 있는
    매우 작은 단위로 분할하여 이를 해결한 이후 기록(Memoization) 이후
    더 큰 단위로 확장하여, 풀이하는 방법
    수학에서의 점화식 f(n) = 2*f(n-1) 과 같이 이전의 해에 어떠한 연산을 통하여 현재의 해를 구한다.
    직관적으로 구할 수 있는 가장 작은 값의 경우 미리 구하여 초기화 해 놓는다.
'''
"""
if __name__ == "__main__":
    n = int(input())
    tmp = [0]*(n+1)

    tmp[1] = 1
    tmp[2] = 2

    for i in range(3, n+1):
        tmp[i] = tmp[i-1]+tmp[i-2]

    print(tmp[n])
"""
'''
    2. Top-Down 방식 : Recursion, Memoization
    큰 문제를 아주 작은단위로 분할하는건 같으나, 이를 재귀를 통한 반복
    실행으로서, 작은 단위부터 점점 큰 단위로 합쳐간다.
    Memoization : 이미 결과를 얻어 별도의 table에 기록이 된 상태에서,
    이와 같은 연산이 다시 수행될 경우, 이에 대한 결과를 테이블에서 곧바로 찾아,
    curedge 하는 방식. 
'''
def REC(len):
    if memo[len] != 0:
        return memo[len]
    # 이미 결과가 얻어진 가장 작은 단위의 결과는 별도로 출력
    if len == 1 or len == 2:
        return len
    # 메모를 하는 구간
    else:
        memo[len] = REC(len-1)+REC(len-2)
        return memo[len]
    
if __name__ == "__main__":
    n = int(input())
    memo = [0]*(n+1)
    print(REC(n))