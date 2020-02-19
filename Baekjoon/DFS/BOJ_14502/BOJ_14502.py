# Problem [14502] : 연구소

import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def combi(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        
        else:
            for next in combi(arr[i+1:], r-1):
                yield [arr[i]] + next

def DFS(x,y):

    copy_d[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if copy_d[nx][ny] == 0:
                DFS(nx,ny)


if __name__ == "__main__":
    N, M = map(int, input().split())
    d = [list(map(int,input().split())) for _ in range(N)]
    zero = [[i,j] for i in range(N) for j in range(M) if d[i][j] == 0]
    virus = [[i,j] for i in range(N) for j in range(M) if d[i][j] == 2]
    m = 0

    for choosen in list(combi(zero,3)):
        cnt = 0
        copy_d = list()
        for col in d:
            copy_d.append(col[:])
        for i in range(3):
            x, y = choosen[i]
            copy_d[x][y] = 1
        for axis in virus:
            x, y = axis
            DFS(x,y)
        for i in range(N):
            for j in range(M):
                if copy_d[i][j] == 0:
                    cnt += 1
        m = max(m,cnt)
    print(m)
        
            
        
