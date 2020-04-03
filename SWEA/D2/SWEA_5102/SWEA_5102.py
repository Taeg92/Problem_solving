# Problem [5102] : 노드의 거리

import sys
sys.stdin = open('input.txt')

def BFS(v,depth):
    global end
    V[v] = 1
    Q = list()
    Q.append((v, depth))

    while Q:
        nxt, d = Q.pop(0)
        if nxt == end:
            return d
        for w in G[nxt]:
            if not V[w]:
                V[w] = 1
                Q.append((w, d+1))
    return 0

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        V, E = map(int, input().split())
        G = [[]*(V+1) for _ in range(V+1)]
        V = [0]*(V+1)
        for _ in range(E):
            u, v = map(int,input().split())
            G[v].append(u)
            G[u].append(v)
        start, end = map(int, input().split())
        result = BFS(start,0)
        print('#{} {}'.format(tc, result))