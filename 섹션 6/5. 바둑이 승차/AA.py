import sys
sys.stdin = open('input.txt','r')
MAX = 0;
def DFS(L, SUM) :
    
    if L == len(W): 
        if C < SUM:
            return
        elif C >= SUM:
            global MAX
            if MAX < SUM:
                MAX = SUM
                return
    else :
        # DFS 는 이러한 원리로 완전탐색을 수행한다.
        DFS(L+1, SUM+W[L])
        DFS(L+1, SUM)

if __name__ == "__main__":

    C, N = map(int, input().split())
    W = list(map(int, input().split()))
    DFS(0, 0)
    print(MAX)