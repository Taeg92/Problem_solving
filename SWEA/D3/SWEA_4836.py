# Problem [4836] : 색칠하기

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())

    for _ in range(N):
        x1, y1, x2, y2 , c= map(int,input().split())
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                arr[x][y] += c
    cnt = 0
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc,cnt))