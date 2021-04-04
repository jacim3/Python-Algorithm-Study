import sys, math
# sys.stdin = open('input.txt','r')

def DFS(level, sum):
    global mini
    if level > l :
        return
    if sum == e:
        if mini > level :
            mini = level 
    else:
        DFS(level+1, sum+5)
        DFS(level+1, sum+1)
        DFS(level+1, sum-1)
        


if __name__ == "__main__":
    mini = 9999
    s, e = map(int, input().split())
    l = math.ceil(e/5)
    DFS(0, s)
    print(mini)