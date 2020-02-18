# Problem [2667] : 단지번호붙이기

import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x,y):

    check[x][y] = 1
    ret = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not check[nx][ny] and d[nx][ny] == 1:
                ret += DFS(nx,ny)
    return ret



if __name__ == "__main__":
    N = int(input())
    d = [list(map(int,list(input()))) for _ in range(N)]
    check = [[0]*N for _ in range(N)]
    result = list()
    for i in range(N):
        for j in range(N):
            if d[i][j] == 1 and not check[i][j]:
                result.append(DFS(i,j))
    result.sort()
    size = len(result)
    print(size)
    for r in result:
        print(r)