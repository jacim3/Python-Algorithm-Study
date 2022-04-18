import sys
sys.stdin = open('input.txt','r')


# 1번 풀이 = 2차원 배열에 경로정보를 배열로서 전부 집어넣고, 간선과 노드 각각을 체크하는 변수를 두어 풀이.
"""
def DFS(level ,start, arr):
    if level > N :
        return
    if start == N:
        # print(arr)
        global count
        count = count+1
    else :

        for i in range(0, M):
            if dict[i][0] == start:
                if check[i] == 0:
                    if check_point[dict[i][1]-1] == 0:
                        check[i] = 1
                        check_point[dict[i][1]-1] = 1
                        arr.append(dict[i])
                        DFS(level+1, dict[i][1], arr)
                        check[i] = 0
                        check_point[dict[i][1]-1] = 0
                        arr.pop()


if __name__ == "__main__":
    count = 0;
    N, M = map(int, input().split())
    dict = []
    check = [0]*M
    check_point = [0]*N
    check_point[0] = 1
    
    for i in range(0, M):
        array = []
        str = input()
        array.append(int(str.split()[0]))
        array.append(int(str.split()[1]))
        dict.append(array)
        
    DFS(0, 1, [])
    print(count)

"""

# 2번 풀이
def DFS(start):

    if start == N:
        print(path)
        global cnt
        cnt = cnt +1 
    else :
        for i in range(1, N+1):
            print(ch)
            if arr[start][i] == 1 and ch[i] == 0:
                # print(arr)
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0
            

if __name__ == "__main__":
    cnt = 0;
    N, M = map(int, input().split())  
    arr = [[0]*(N+1) for _ in range(N+1)]
    ch = [0]*(N+1)
    ch[1] = 1
    path = []
    path.append(1)
    for i in range(M):
        a,b = map(int, input().split())
        arr[a][b] = 1
    DFS(1)
    print(cnt)