# Problem [15650] : N과 M(2)

import sys
sys.stdin = open('input.txt')

def combination(arr, n, s):
    if n == M:
        print(*result)
        return
    else:
        for i in range(s, N):
            if not C[i]:
                C[i] = 1
                result.append(arr[i])
                combination(arr,n+1,i+1)
                result.pop()
                C[i] = 0

if __name__ == "__main__":
    N, M = map(int,input().split())
    C = [0]*N
    result = list()
    combination(range(1,N+1), 0, 0)