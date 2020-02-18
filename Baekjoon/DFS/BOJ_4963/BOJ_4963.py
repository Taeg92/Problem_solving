# Problem [4963] : 섬의 개수

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(50*50)

def DFS(c,r):

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        x = c + dx[i]
        y = r + dy[i]
        if 0 <= x <= h-1 and 0 <= y <= w-1:
            if not check[x][y] and data[x][y] == 1:
                check[x][y] = 1
                DFS(x,y)


while 1:
    w, h = map(int,input().split())
    if not w and not h:
        break
    data = [list(map(int,input().split())) for _ in range(h)]
    check = [[0]*w for _ in range(h)]
    cnt = 0 

    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and not check[i][j]:
                DFS(i,j)
                cnt += 1
    print(cnt)