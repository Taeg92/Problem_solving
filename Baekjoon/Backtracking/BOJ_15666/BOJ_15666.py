# Problem [15666] : N과 M(12)

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

def repeat_combi(arr, n, s):
    if n == M:
        result.append(tuple(temp[:]))
        return
    else:
        for i in range(s,N):
            temp.append(arr[i])
            repeat_combi(arr, n+1, i)
            temp.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    D = sorted(list(map(int,input().split())))
    temp = list()
    result = list()
    repeat_combi(D, 0, 0)
    result = sorted(list(set(result)))
    for r in result:
        print(*r)