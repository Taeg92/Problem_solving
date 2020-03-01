# Problem [15652] : N과 M(4)

import sys
sys.stdin = open('input.txt')

def repeat_conbi(arr, n, s):
    if n == M:
        print(*result)
    else:
        for i in range(s,N):
            result.append(arr[i])
            repeat_conbi(arr,n+1,i)
            result.pop()

if __name__ == "__main__":
    N, M = map(int,input().split())
    result = list()
    repeat_conbi(range(1,N+1),0,0)