# Problem [15657] : N과 M(8)

import sys
sys.stdin = open('input.txt')

def repeat_combi(arr, n, s):
    if n == M:
        print(*result)
        return
    else:
        for i in range(s,N):
            result.append(arr[i])
            repeat_combi(arr, n+1, i)
            result.pop()
            
if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    result = list()
    repeat_combi(D, 0, 0)