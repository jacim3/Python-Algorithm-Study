import sys
# sys.stdin = open('input.txt','rt')

n = int(input())
scores = list(map(int, input().split()))

# sum() 은 list의 값을 모두 더한값을 반환
# round() 는 소수 1째 자리에서 반올림
# 파이썬의 경우는 round_half_up 방식이 아닌 round_half_even 방식이므로, 
# 즉 4.500의 경우 전자는 반올림을 하나, 후자의 경우 중간값일 경우 짝수쪽에 근사한 값으로 이동한다.
# 그러므로 0.5를 더하고 int()로 변환하는 방식을 사용할 것 !!!
avr = round(sum(scores)/n)

dic = {}
# 열거 -> 루프를 인덱스와 값으로 분할하여 나열할 수 있게 하며,
# 이를 dictionary 에 곧바로 집어넣는다.
for idx, x in enumerate(scores):
    dic[idx+1] = x -avr

min = 101
score = 0
index = 0
value = 0

for i,v in dic.items():

    if min > abs(v):  
        min = abs(v)
        index = i
        value = v
    elif abs(min) == abs(v):
        if v > value:
            index = i
            value = v
        
print(avr, index)
