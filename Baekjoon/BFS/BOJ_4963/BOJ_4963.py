# Problem [4963] : 섬의 개수

import sys
sys.stdin = open('input.txt')

def BFS(c,r):
    queue = list()
    queue.append([c,r])
    check[c][r] = 1

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    while queue:

        col, row = queue.pop(0)
        for i in range(8):
            x = col + dx[i]
            y = row + dy[i]
            if 0 <= x <= h-1 and 0 <= y <= w-1:
                if not check[x][y] and data[x][y] == 1:
                    queue.append([x,y])
                    check[x][y] = 1


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
                BFS(i,j)
                cnt += 1
    
    print(cnt)
    