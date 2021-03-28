import sys, math
from collections import deque
# sys.stdin = open('input.txt','rt')

# 인터프리터 내에서 직접 실행했을 때만, if문 내의 코드를 실행해라
if __name__ == "__main__":
    
    n = 10000
    # 한번 이동한 지점을 다시 지나가지 않도록 방지 = 최단거리를 구해야 하므로
    check = [0]*(n+1)
    # BFS의 특징으로, Level 값을 저장
    check2 = [0]*(n+1)
    move = [5,-1,1]
    s,e = map(int, input().split())
    song = deque()
    song.append(s)
    check[s] = 1

    while song:
        start = song.popleft()

        if start == e:
            break
        for i in move:
            next = start+i
            if 0<next<=n:
                if check[next] == 0:
                    check[next] = 1

                    song.append(next)
                    check2[next] = check2[start]+1

    print(check2[e])