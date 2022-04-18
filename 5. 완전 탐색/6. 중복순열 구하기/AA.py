import sys, math
# sys.stdin = open('input.txt','rt')

def DFS(L, VAL):
    if L == N:
        print(VAL) 
        global count
        count = count+1
    else :
        for i in range(1, M+1):
            DFS(L+1, VAL+str(i)+" ")



# 인터프리터 내에서 직접 실행했을 때만, if문 내의 코드를 실행해라
if __name__ == "__main__":
    M, N = map(int, input().split())
    count = 0
    DFS(0, "")
    print(count)