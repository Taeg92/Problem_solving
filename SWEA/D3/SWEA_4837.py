# Problem [4837] : 부분집합의 합

import sys

sys.stdin = open('input.txt')

def combination(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:],r-1):
                yield [arr[i]] + next


T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    cnt = 0
    for factor in combination(range(1,13),N):
        if sum(factor) == K:
            cnt += 1
    print('#{} {}'.format(tc,cnt))