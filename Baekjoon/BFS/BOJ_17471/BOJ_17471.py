#Problem [17471] : 게리맨더링

from itertools import combinations as combi
from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

m = sys.maxsize

def connected(area):
    
    if len(area) == 1:
        return True
    
    else:
        C = [0]*(N+1)
        depth = 1
        queue = deque()
        queue.append(area[0])
        C[area[0]] = 1

        while queue:

            q = queue.popleft()
            for w in G[q]:
                if not C[w] and w in area:
                    C[w] = 1
                    queue.append(w)
                    depth += 1
        
        if depth == len(area):
            return True
        return False
        


def diff_population(area1,area2):
    global m
    if connected(area1) and connected(area2):
        s = 0
        for i in range(len(area1)):
            s += P[area1[i]]
        for i in range(len(area2)):
            s -= P[area2[i]]
        s = abs(s)
        if m > s:
            m = s
    return m


if __name__ == "__main__":
    N = int(input())
    P = [0] + list(map(int,input().split()))
    G = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        u, *v = map(int,input().split())
        G[i].extend(v)

    for i in range(1, N//2 + 1):
        for area1 in combi(range(1, N+1), i):
            area2 = [i for i in range(1,N+1) if i not in area1]
            diff_population(area1,area2)
    if m == sys.maxsize:
        print(-1)
    else:
        print(m)