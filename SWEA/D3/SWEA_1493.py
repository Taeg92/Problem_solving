# Problem [1493] : 수의 새로운 연산

import sys

sys.stdin = open('input.txt')

def find_axis(n):
    x = 1 
    y = 1
    cnt = 1
    while 1:
        if y < 1:
            y = x
            x = 1
        if cnt == n:
            break
        x += 1
        y -= 1
        cnt += 1
    return x,y  

def find_n(a,b):
    x = 1 
    y = 1
    cnt = 1
    while 1:
        if y < 1:
            y = x
            x = 1
        if x == a and y == b:
            break
        x += 1
        y -= 1
        cnt += 1
    return cnt 



T = int(input())
for tc in range(1, T+1):
    p, q = map(int,input().split())
    x1, y1 = find_axis(p)
    x2, y2 = find_axis(q)
    x = x1 + x2
    y = y1 + y2
    print('#{} {}'.format(tc,find_n(x,y)))