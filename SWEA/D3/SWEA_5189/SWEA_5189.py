# Problem [5189] : 전자카트

import sys
sys.stdin = open('input.txt')

def DFS(x, n, val):
    global m
    if m <= val:
        return
    if n == N-1:
        val += D[x][0]
        m = min(val, m)
    for nxt in range(0,N):
        if not V[nxt]:
            V[nxt] = 1
            DFS(nxt, n+1, val+D[x][nxt])
            V[nxt] = 0

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = [list(map(int,input().split())) for _ in range(N)]
        V = [0]*(N)
        m = float('inf')
        V[0] = 1
        DFS(0, 0, 0)
        print('#{} {}'.format(tc, m))
