# Problem[1248] : 공통조상

import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    V, E, n1, n2 = map(int, input().split())
     
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if L[arr[i]]:
            R[arr[i]] = arr[i + 1]
        else:
            L[arr[i]] = arr[i + 1]
        P[arr[i + 1]] = arr[i]
 
    def findLCA():
        visit = set()
        p = P[n1]
        while p:
            visit.add(p)
            p = P[p]
        p = P[n2]
        while p:
            if p in visit: return p
            p = P[p]
             
    def treeSize(v):
        if v == 0: return 0
         
        l = treeSize(L[v])
        r = treeSize(R[v])
        return l + r + 1
         
    lca = findLCA()
     
    print('#{} {} {}'.format(tc, lca, treeSize(lca)))