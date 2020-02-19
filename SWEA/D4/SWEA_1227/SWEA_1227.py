# Problem [1226] : 미로2

import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y):
    Possible = 0
    Queue = list()
    check[x][y] = 1
    Queue.append([x,y])

    while Queue:

        cx, cy = Queue.pop(0)
        if data[cx][cy] == 3:
            Possible = 1

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (1 <= nx <= 99) and (1 <= ny <= 99):
                if not check[nx][ny] and data[nx][ny] == 0 or data[nx][ny] == 3:
                    Queue.append([nx,ny])
                    check[nx][ny] = 1
    return Possible

for tc in range(1, 11):
    T = int(input())
    data = [list(map(int,list(input()))) for _ in range(100)]
    check = [[0]*(100) for _ in range(100)]
    result = BFS(1,1)
    print('#{} {}'.format(T,result))