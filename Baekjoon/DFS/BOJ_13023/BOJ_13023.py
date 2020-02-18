# Problem [13023] : ABCDE

import sys
sys.stdin = open('input.txt')

def DFS(v, depth):
    global isPossible
    if depth == 4:
        isPossible = 1
        return
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            DFS(w,depth+1)
            if isPossible:
                return
    visited[v] = 0



if __name__ == "__main__" :
    V, E = map(int,input().split())
    G = [[] for _ in range(V)]
    visited = [0]*V
    isPossible = 0
    for _ in range(E):
        u, v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)

    for i in range(E):
        DFS(i,0)
        if isPossible:
            break
    
    print(int(isPossible))