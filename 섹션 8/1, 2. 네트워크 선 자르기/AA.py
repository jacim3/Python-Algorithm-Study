import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')
'''
    Dynamic programming
    1. Bottom-Up 방식
    풀이가 불가능할 정도로 규모가 큰 문제를 우리가 직관적으로 알아볼 수 있는
    매우 작은 단위로 분할하여 이를 해결한 이후 기록(Memoization) 이후
    더 큰 단위로 확장하여, 풀이하는 방법
    수학에서의 점화식 f(n) = 2*f(n-1) 과 같이 이전의 해에 어떠한 연산을 통하여 현재의 해를 구한다.
    직관적으로 구할 수 있는 가장 작은 값의 경우 미리 구하여 초기화 해 놓는다.
'''
if __name__ == "__main__":
    n = int(input())
    tmp = [0]*(n+1)

    tmp[1] = 1
    tmp[2] = 2

    for i in range(3, n+1):
        tmp[i] = tmp[i-1]+tmp[i-2]

    print(tmp[n])