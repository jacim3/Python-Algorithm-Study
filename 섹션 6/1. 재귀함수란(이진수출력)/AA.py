import sys
# sys.stdin = open('input.txt','rt')


# 1. Java에서 사용하는 방식을 이용
"""
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

"""

# 2. Python의 방식을 이용
# 재귀함수의 원리는 Stack을 이용하여 함수의 호출 정보들을 기록을 한 이후, 순차적으로 함수가 작동하며, 이는 DFS(깊이우선)의 방식을 따른다.
# 함수는 자신의 역할이 끝날 때 까지는 도중에 다른 함수가 호출된다 하더라도, 종료되지 않고 스택에 저장된다. 
def DFS(x):
    if x ==0:
        return
    else:
        
        DFS(x//2)
        print(x%2, end=' ')

# 인터프리터 내에서 직접 실행했을 때만, if문 내의 코드를 실행해라
if __name__ == "__main__":
    n = int(input())
    DFS(n)


