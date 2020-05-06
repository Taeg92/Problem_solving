# Problem [5188] : 최소합

import sys
sys.stdin = open('input.txt')

dx = (1, 0)
dy = (0, 1)
def DFS(x, y, n, val):
    global m
    if m <= val:
        return
    if n == 2*N-2:
        m = min(val, m)
        return
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            DFS(nx, ny, n+1, val+D[nx][ny])

    
if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = [list(map(int, input().split())) for _ in range(N)]
        m = float('inf')
        DFS(0,0,0,D[0][0])
        print('#{} {}'.format(tc, m))