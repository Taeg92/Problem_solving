# Problem [15649] : N과 M(1)

import sys
sys.stdin = open('input.txt')

# nPm
def permutation(arr, r):

    if r == M:
        print(*result)
        return
    
    else:
        for i in range(N):
            if not C[i]:
                C[i] = 1
                result.append(arr[i])
                permutation(arr, r+1)
                result.pop()
                C[i] = 0


if __name__ == "__main__":
    N, M = map(int,input().split())
    C = [0]*(N)
    result = list()
    permutation(range(1,N+1), 0)