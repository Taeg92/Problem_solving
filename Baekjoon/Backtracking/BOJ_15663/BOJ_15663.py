# Problem [15663] : N과 M(9)

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

def permutation(arr,n):
    if n == M:
        result.append(tuple(temp[:]))
        return
    else:
        for i in range(N):
            if not C[i]:
                C[i] = 1
                temp.append(arr[i])
                permutation(arr, n+1)
                temp.pop()
                C[i] = 0

if __name__ == "__main__": 
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    C = [0]*N
    temp = list()
    result = list()
    permutation(D, 0)
    result = sorted(list(set(result)))
    for r in result:
        print(*r)