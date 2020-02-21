# Problem [2651] : 자동차경주대회

import sys
sys.stdin = open('input.txt')
Big_N = sys.maxsize

if __name__ == "__main__":
    L = int(input())
    N = int(input())
    A = [0]*(N+2)
    d = list(map(int,input().split()))
    T = [0] + list(map(int,input().split())) + [0]
    D = [Big_N] * (N+2)
    check = [0]*(N+2)
    R = [[] for _ in range(N+2)]
    
    for i in range(1,N+2):
        A[i] += A[i-1] + d[i-1]

    D[0] = 0
    for i in range(1,N+2):
        for j in range(i-1, -1, -1):
            if A[i] - A[j] <= L and D[j] + T[i] < D[i]:
                D[i] = D[j] + T[i]
                check[i] = check[j] + 1
                R[i] = R[j] + [str(i)]
    print(D[-1])
    print(check[-1]-1)
    print(' '.join(R[-1][:-1]))    