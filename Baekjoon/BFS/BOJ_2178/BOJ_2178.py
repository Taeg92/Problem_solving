# Problem [2178] : 미로 탐색

import sys
sys.stdin = open('input.txt')

def BFS(c,r):
    Queue = list()
    check = [[0]*(M+1) for _ in range(N+1)]
    check[c][r] = 1
    dist = 1
    Queue.append([c,r,dist])


    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dt = 1
    while Queue:

        col, row, dist = Queue.pop(0)
        if col == N and row == M:
            return dist

        for i in range(4):
            x = col + dx[i]
            y = row + dy[i]
            d = dist + dt
            if (1 <= x <= N) and (1 <= y <= M):
                if not check[x][y] and data[x-1][y-1] == 1:
                    Queue.append([x,y,d])
                    check[x][y] = 1
                    


N, M = map(int,input().split())
data = [list(map(int,list(input()))) for _ in range(N)]
result = BFS(1,1)
print(result)