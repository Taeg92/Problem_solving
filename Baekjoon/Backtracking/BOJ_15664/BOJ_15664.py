# Problem [15664] : N과 M(10)

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

def combination(arr, n, s):
    if n == M:
        result.append(tuple(temp[:]))
        return
    
    else:
        for i in range(s,N):
            if not C[i]:
                C[i] = 1
                temp.append(arr[i])
                combination(arr, n+1, i+1)
                temp.pop()
                C[i] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    D = sorted(list(map(int,input().split())))
    C = [0]*N
    temp = list()
    result = list()
    combination(D, 0, 0)
    result = sorted(list(set(result)))
    for r in result:
        print(*r)
