import sys
# sys.stdin = open('input.txt','r')

def DFS(remain, arr):
    global count
    if len(remain) == 0 :
        for i in arr:
            print(ch(i), end="")
        print()
        count +=1
    else :
        for i in range (1, 3):

            if len(remain) < i:
                return

            val = int(remain[0:i])
            rem = remain[i:]
            if val <=26 :
                arr.append(val)
                DFS(rem, arr)
                arr.pop()

def ch(number):
    return chr(number+64)

if __name__ == "__main__":
    count = 0
    password = input()
    storage = []
    DFS(password, [])
    print(count)
  