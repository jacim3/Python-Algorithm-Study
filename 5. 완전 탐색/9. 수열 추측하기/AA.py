import sys
# sys.stdin = open('input.txt','r')

def DFS(level, sum, art):

    if level == N:
        if sum == F:
            for i in art :
                print(i, end=' ')
            print()
            sys.exit(0)
    else :
        for i in range(1, N+1):

            if ch[i-1] == 0 :
                ch[i-1] = 1
                art.append(i)
                DFS(level+1, sum+i* arr[level], art)
                art.pop()
                ch[i-1] = 0
            

if __name__ == "__main__":
    N, F = map(int, input().split())

    arr = [1]*N
    ch = [0]*N
    art = []
    for i in range(1, N):
        arr[i] = int(arr[i-1]*(N-i)/i);         #  

    tmp = [i for i in range(1,N+1)]             # 1~N 까지의 값이 들어가도록 배열을 한꺼번에 초기화
    DFS(0, 0, art)
    