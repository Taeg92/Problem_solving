# Problem [14888] : 연산자 끼워넣기

import sys
sys.stdin = open('input.txt')

min_val = sys.maxsize
max_val = -sys.maxsize

def BT(n,s):
    # [+, -, X, /]
    global min_val, max_val
    if n == N:
        min_val = min(min_val, s)
        max_val = max(max_val, s)
    
    else:
        for i in range(4):
            if operator[i]:
                operator[i] -= 1
                if i == 0:
                    BT(n+1, s + d[n])
                elif i == 1:
                    BT(n+1, s - d[n])
                elif i == 2:
                    BT(n+1, s * d[n])
                else:
                    if s < 0:
                        BT(n+1, -(abs(s)//d[n]))
                    else:
                        BT(n+1, s // d[n])
                operator[i] += 1

if __name__ == '__main__':
    N = int(input())
    d = list(map(int,input().split()))
    operator = list(map(int,input().split()))
    BT(1, d[0])
    print(max_val)
    print(min_val)