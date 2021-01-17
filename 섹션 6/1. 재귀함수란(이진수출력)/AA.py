import sys
# sys.stdin = open('input.txt','rt')

n = int(input())
list = []

def trans(ins):
    if int(ins / 2) == 1:
        list.append(int(ins%2))
        return list.append(1)

    list.append(int(ins%2))
    ins =  ins/2

    trans(ins) 

trans(n)

for i in reversed(list):
    print(i, end="")