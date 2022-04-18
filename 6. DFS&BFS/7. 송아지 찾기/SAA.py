import sys, math
from collections import deque
# sys.stdin = open('input.txt','r')

"""
    BFS 는 레벨탐색 및 Queue를 사용한다.
    보통의 list의 경우 append 및 pop() 을 사용하게 되는 경우, FILO 로서 stack 의 원리를 가짐
    이를 해결하기 위하여 pop(0)을 사용하게 될 경우, queue 를 구현할 수 있으나, 작업시간이 오래 걸리게 된다.
"""

if __name__ == "__main__":

    s, e = map(int, input().split())
    MAX = 10000
    steps = [5, 1, -1]
    dis = [0] * (MAX+1)
    check = [0] * (MAX+1)
    check[s] = 1
    dis[s] = 0
    
    dQ = []
    dQ.append(s)

    while dQ:
        now = dQ.pop(0)
        if now == e:
            break
        for step in steps:
            next = now + step
            if 0<next<MAX:
                if check[next] == 0:
                    dQ.append(next)
                    check[next] = 1
                    dis[next] = dis[now]+1
    print(dis[e])

