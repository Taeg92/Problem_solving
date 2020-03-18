# Problem [2814] : 최장 경로

import sys
sys.stdin = open('input.txt')

def DFS(v, depth):
    global m

    if depth > m:
        m = depth

    visited[v] = 1

    for w in G[v]:
        if not visited[w]:
            DFS(w, depth+1)
            
    visited[v] = 0



if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        V, E = map(int,input().split())
        G = [[] for _ in range(V+1)]
        m = 0
        visited = [0]*(V+1)
        for _ in range(E):
            u, v = map(int,input().split())
            G[u].append(v)
            G[v].append(u)
        
        for i in range(1, V+1):
            DFS(i,1)
        
        print('#{} {}'.format(tc, m))