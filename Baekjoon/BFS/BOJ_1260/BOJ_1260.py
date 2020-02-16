# Problem [1260] : DFS와 BFS

import sys

sys.stdin = open('input.txt')

def dfs(u):

    check[u] = 1
    result.append(u)

    for v in G[u]:
        if not check[v]:
            dfs(v)

def bfs(u):
    queue = list()
    queue.append(u)
    check[u] = 1

    while queue:     
        u = queue.pop(0)
        result.append(u)
        for v in G[u]:
            if not check[v]:
                check[v] = 1
                queue.append(v)


V, E, n = map(int,input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

for v in G:
    v.sort()

result = list()
check = [0]*(V+1)
dfs(n)
print(*result) 
result = list()
check = [0]*(V+1)  
bfs(n)
print(*result) 