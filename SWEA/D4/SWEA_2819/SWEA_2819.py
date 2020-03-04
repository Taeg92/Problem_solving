# Problem [2819] : 격자판의 숫자 이어 붙이기

import sys
sys.stdin = open('input.txt')

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
def DFS(x,y,s):
    if len(s) == 7:
        R.add(s)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            DFS(nx,ny,s+D[nx][ny])

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        D = [tuple(input().split()) for _ in range(4)]
        R = set()
        for i in range(4):
            for j in range(4):
                DFS(i, j, D[i][j])
        print('#{} {}'.format(tc,len(R)))