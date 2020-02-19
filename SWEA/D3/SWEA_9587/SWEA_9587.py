# Problem [9587] : 그래프 경로2

import sys
sys.stdin = open('input.txt')

def DFS(start,end):
    global Possible
    check[start] = 1
    if start == end:
        Possible = 1
    
    for w in G[start]:
        if not check[w]:
            DFS(w,end)
    check[v] = 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    check = [0]*(V+1)
    Possible = 0
    for _ in range(E):
        u, v = map(int,input().split())
        G[u].append(v)
    start, end = map(int,input().split())
    DFS(start,end)
    print('#{} {}'.format(tc,Possible))
    