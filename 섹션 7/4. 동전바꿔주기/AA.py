import sys
# sys.stdin = open('input.txt','r')

def DFS(level, sum, st):
    if level == L:
        if sum == 20:
            total.append(st)
    else:
        DFS(level+1, sum+dic[level], st+str(dic[level])+" ")
        DFS(level+1, sum, st)

if __name__ == "__main__":
    T = int(input())
    K = int(input())
    dic = []
    L = 0
    total = []
    for i in range(K):
        P, N = map(int, input().split())
   
        L = L+N

        for j in range(N):
            dic.append(P)

    
    DFS(0,0,"")
    # print(total)
    sss = set(total)
    # print(sss)
    print(len(sss))