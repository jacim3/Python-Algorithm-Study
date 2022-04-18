import sys
# sys.stdin = open('input.txt','r')

def DFS(level, start, arr):
    if level == M:
        for i in arr:
            print(i, end="")
        print()
        global count
        count = count+1
    else :
        
        for i in range(start, N+1):
            arr.append(i)
            DFS(level+1, i+1, arr)
            arr.pop()
         

if __name__ == "__main__":
    count = 0;
    N, M = map(int, input().split())
    arr = []
    DFS(0, 1, arr)
    print(count)