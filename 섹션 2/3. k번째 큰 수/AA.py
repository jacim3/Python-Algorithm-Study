import sys
# sys.stdin = open('input.txt','rt')

n, k = map(int, input().split())
array = list(map(int, input().split()))    
# 중복을 제거하는 자료구조인 set()을 사용해야 한다.
# 완전탐색의 하나로서, 모든 경우의 수를 위하여 모든 값을 참조해야 한다.
res = set()
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1, n):
            res.add(array[i]+array[j]+array[l])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
