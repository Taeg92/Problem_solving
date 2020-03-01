# Problem [15665] : N과 M(11)

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

def product(arr, n):
    if n == M:
        result.append(tuple(temp[:]))
    else:
        for i in range(N):
            temp.append(arr[i])
            product(arr,n+1)
            temp.pop()

if __name__ == "__main__":
    N, M = map(int,input().split())
    D = sorted(list(map(int,input().split())))
    temp = list()
    result = list()
    product(D, 0)
    result = sorted(list(set(result)))
    for r in result:
        print(*r)
    