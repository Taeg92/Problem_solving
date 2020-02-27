# Problem [1486] : 장훈이의 높은 선반

import sys
sys.stdin = open('input.txt')

def DFS(n,v):
    global m
    if n == N:
        if v >= B:
            m = min(m,v)
        return
    DFS(n+1, v + D[n])
    DFS(n+1, v)


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, B = map(int,input().split())
        D = list(map(int,input().split()))
        m = float('inf')
        DFS(0,0)
        print('#{} {}'.format(tc,m-B))