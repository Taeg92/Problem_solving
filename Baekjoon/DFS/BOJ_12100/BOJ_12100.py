# Problem [12100] : 2048 (Easy)

from copy import deepcopy
import sys
sys.stdin = open('input.txt')

dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)
def move(arr, dir):
    check = [[0]*N for _ in range(N)]
    if dir in (0, 1):
        spos, epos, step = 0, N, 1
    else:
        spos, epos, step = N-1, -1, -1

    for i in range(spos,epos,step):
        for j in range(spos,epos,step):
            if arr[i][j] == 0:
                continue
            x, y = i, j
            val = arr[x][y]
            arr[x][y] = 0
            nx, ny = x + dx[dir], y + dy[dir]

            while 1:
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if arr[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dx[dir], y + dy[dir]
                
                elif arr[nx][ny] == val and not check[nx][ny]:
                    x, y = nx, ny
                    check[x][y] = 1
                    break
                else:
                    break
            arr[x][y] = arr[x][y] + val
    return arr

def DFS(n,arr):
    global m
    if n == N:
        for col in arr:
            m = max(m,max(col))
        return
    else:
        for i in range(4):
            temp = deepcopy(arr)
            arr = move(arr,i)
            DFS(n+1,arr)
            arr = deepcopy(temp)

            

if __name__ == "__main__":
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    m = 0
    DFS(0,D)
    print(m)