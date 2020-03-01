# Problem [15654] : N과 M(5)

import sys
sys.stdin = open('input.txt')

def permutation(arr, n):
    if n == M:
        print(*result)
        return
    else:
        for i in range(N):
            if not C[i]:
                C[i] = 1
                result.append(D[i])
                permutation(arr,n+1)
                result.pop()
                C[i] = 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    C = [0]*N
    result = list()
    permutation(D, 0)