import sys
# sys.stdin = open('input.txt','rt')

t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    array = list(map(int, input().split()))
    array = array[s-1:e]
    array.sort()
    print('#%d %d' %(i+1, array[k-1]))
    




