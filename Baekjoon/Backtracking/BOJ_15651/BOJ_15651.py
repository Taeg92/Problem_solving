# Problem [15651] : N과 M(3)

import sys
sys.stdin = open('input.txt')

def product(arr, r):

    if r == M:
        print(*result)
        return
    else:
        for i in range(N):
            result.append(arr[i])
            product(arr,r+1)
            result.pop()

if __name__ == "__main__":
    N, M = map(int,input().split())
    result = list()
    product(range(1, N+1), 0)