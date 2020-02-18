# Problem [13023] : ABCDE

import sys
sys.stdin = open('input.txt')


def dfs(node, depth):
    global possible
    visited[node] = 1
    if (depth == 4):
        possible = True
        return
    for x in v[node]:
        if visited[x] == 0:
            dfs(x, depth+1)
            if (possible):
                return
    visited[node] = 0


if __name__ == "__main__":
    N, M = map(int,input().split())
    v = [[] for _ in range(N)]
    visited = [0]*N
    possible = False


    for _ in range(M):
        a, b = map(int,input().split())
        v[a].append(b)
        v[b].append(a)
    
    for i in range(N):
        dfs(i, 0)
        if (possible):
            break
    if (possible):
        print(1)
    else: print(0)