# Problem [5656] : [모의 SW 역량테스트] 벽돌 깨기

from collections import deque
from copy import deepcopy
import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(n, arr):
    copy_Arr = deepcopy(arr)
    queue = deque()
    for i in range(H):
        if copy_Arr[i][n]:
            if copy_Arr[i][n] == 1:
                copy_Arr[i][n] = 0
            else:
                queue.append((i, n, copy_Arr[i][n]))
                copy_Arr[i][n] = 0
            break
    while queue:
        cx, cy, d = queue.popleft()
        for n in range(1, d):
            for i in range(4):
                nx = cx + dx[i]*n
                ny = cy + dy[i]*n
                if 0 <= nx < H and 0 <= ny < W:
                    if copy_Arr[nx][ny]:
                        if copy_Arr[nx][ny] == 1:
                            copy_Arr[nx][ny] = 0
                        else:
                            queue.append((nx, ny, copy_Arr[nx][ny]))
                            copy_Arr[nx][ny] = 0
    copy_Arr = pull(copy_Arr)
    return copy_Arr
 
def DFS(n, arr):
    global m
    if m == 0:
        return
    if n == N:
        m = min(m,total(arr))
    else:
        for i in range(W):
            DFS(n+1,BFS(i,arr))
 
def pull(arr):
    for i in range(W):
        pos = H - 1
        for j in range(H-1, -1, -1):
            if arr[j][i]:
                arr[j][i], arr[pos][i] = arr[pos][i], arr[j][i]
                pos -= 1
    return arr
     
def total(arr):
    s = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                s += 1
    return s
 
if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, W, H = map(int, input().split())
        D = [list(map(int,input().split())) for _ in range(H)]
        m = float('inf')
        DFS(0,D)
        print('#{} {}'.format(tc,m))