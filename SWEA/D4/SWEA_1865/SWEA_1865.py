# Problem [1865] : 동철이의 일 분배

import sys
sys.stdin = open('input.txt')

def DFS(n,v):
    global m
    if v <= m:
        return
    if n == N:
        m = max(m,v)
        return
    else:
        for i in range(N):
            if not C[i]:
                C[i] = 1
                DFS(n+1,v*(D[n][i]/100))
                C[i] = 0

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = [list(map(int,input().split())) for _ in range(N)]
        C = [0]*N
        m = 0
        DFS(0,1)
        print('#{} {:0.6f}'.format(tc,m*100))