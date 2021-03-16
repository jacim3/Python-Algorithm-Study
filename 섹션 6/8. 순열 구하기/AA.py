import sys
# sys.stdin = open('input.txt','r')

def DFS(l, array, check) :
    global cnt
    if l == M:
        for i in array:
            print(i, end=" ")
        print()
        cnt = cnt+1
        return
    else : 
        for i in range(1, N+1):
            if check[i-1] != 1:
                array[l] = i
                check[i-1] = 1
                DFS(l+1, array, check)
                check[i-1] = 0


if __name__ == "__main__":
    cnt = 0
    N,M = map(int, input().split())
    arr = [0]*M
    ch = [0]*(N)
    DFS(0 , arr, ch)
    print(cnt)