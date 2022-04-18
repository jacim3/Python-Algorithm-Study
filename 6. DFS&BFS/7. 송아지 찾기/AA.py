import sys
from collections import deque

#sys.stdin = open("aaa.txt", "rt")

# 재귀를 통해 구현하려 하였으나, 시간초과 발생. -> BFS 사용 필요.
# 같은 지점으로 돌아가는건 연산 낭비 이므로, 이를 방지해야 함.
# BFS는 너비위주로 탐색하므로, 최단거리를 찾는데 유리.

if __name__ == '__main__':
    command = [1, -1, 5]
    MAX = 10000

    S, E = map(int, input().split())
    check = [0] * (MAX + 1)  # 다시 방문하지 않도록 체크
    distance = [0] * (MAX + 1)  # 이동 횟수 저장

    check[S] = 1
    distance[S] = 0

    dQ = deque()
    dQ.append(S)
    while dQ:
        now = dQ.popleft()
        if now == E:
            break
        for step in command:
            next_step = now+step
            if 0 < next_step < MAX:

                if check[next_step] == 0:
                    dQ.append(next_step)
                    check[next_step] = 1
                    distance[next_step] = distance[now] + 1

    print(distance[E])
