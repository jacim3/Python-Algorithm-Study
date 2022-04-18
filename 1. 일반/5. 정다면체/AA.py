import sys
# sys.stdin = open('input.txt','rt')

n,m = map(int, input().split())

dic = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        try: dic[i+j] = dic[i+j]+1
        except KeyError: dic[i+j] = 1

max = 0
for i,v in dic.items():
    if v > max:
        max = v

for i,v in dic.items():
    if max == v:
        print(i, end=' ')

