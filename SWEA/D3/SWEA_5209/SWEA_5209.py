# Problem [5209] : 최소 생산 비용

import sys
sys.stdin = open('input.txt')

def BT(n, v):
    global m
    if m <= v:
        return
    if n == N:
        m = min(m, v)
        return
    
    for i in range(N):
        if not C[i]:
            C[i] = 1
            BT(n+1, v+D[n][i])
            C[i] = 0

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = [list(map(int, input().split())) for _ in range(N)]
        C = [0]*N
        m = float('inf')
        BT(0, 0)
        print('#{} {}'.format(tc, m))
