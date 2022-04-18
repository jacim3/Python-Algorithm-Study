import sys


# sys.stdin = open("aaa.txt", "rt")


# 올바른 추상화 과정이 중요.
# 1. 어떤 상담을 수행한 경우 해당 날짜를 포함한 날짜 만큼 다음 상담 수행이 불가.
# 2. 마지막 날짜에 해당하는 상담에 소요시간이 1이 아닌경우 수행 불가. -> 중요
def rec(level, point):
    global MAX, N
    if level == N:
        if MAX < point:
            MAX = point
    else:
        # 상담 소요 날짜 만큼 재귀를 이동 및 전체 날짜 N을 넘어가지 않도록 예외 처리 수행.
        if level + T[level] <= N:
            rec(level + T[level], point + P[level])
        rec(level + 1, point)


if __name__ == '__main__':
    N = int(input())
    T = []
    P = []

    MAX = 0
    for i in range(N):
        t, p = map(int, input().split())
        P.append(p)
        T.append(t)

    rec(0, 0)
    print(MAX)
