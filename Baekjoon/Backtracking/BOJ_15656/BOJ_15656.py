# Problem [15656] : N과 M(7)

import sys
sys.stdin = open('input.txt')

def product(arr, n):
    if n == M:
        print(*result)
        return

    else:
        for i in range(N):
            result.append(arr[i])
            product(arr, n+1)
            result.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    result = list()
    product(D, 0)