# Problem [2660] : 회장 뽑기

from collections import deque
import sys
sys.stdin = open('input.txt')

def BFS(s,e):
    check = [0]*(V+1)
    queue = deque()
    depth = 0
    check[s] = 1
    queue.append([s,depth])

    while queue:
        v, d = queue.popleft()
        if v == e:
            break
        for w in G[v]:
            if not check[w]:
                check[w] = 1
                queue.append([w,d+1])
    return d


if __name__ == '__main__':
    V = int(input())
    G = [[] for _ in range(V+1)]
    result = list()
    m = sys.maxsize
    while 1:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break
        G[u].append(v)
        G[v].append(u)
    
    for i in range(1,V+1):
        depth = 0
        for j in range(1,V+1):
            depth = max(depth,BFS(i,j))
        m = min(m,depth)
        result.append([i,depth])
    r = [result[i][0] for i in range(len(result)) if result[i][1] == m]
    r.sort()
    print(m,len(r))
    print(*r)