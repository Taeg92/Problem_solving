#Problem [4839] : 이진탐색

import sys

sys.stdin = open('input.txt')

T = int(input())

def binary_cnt(P,answer):
    start = 1
    end = P
    cnt = 1
    while start <= end:
        mid = (start+end)//2
        if mid == answer:
            break
        elif mid < answer :
            start = mid
        elif mid > answer :
            end = mid
        cnt += 1
    return cnt
        
for tc in range(1, T+1):
    P, A, B = map(int,input().split())
    cnt_A = 0
    cnt_B = 0
    result = ''
    cnt_A = binary_cnt(P,A)
    cnt_B = binary_cnt(P,B)
    if cnt_A > cnt_B :
        result = 'B'
    elif cnt_A == cnt_B:
        result = '0'
    else:
        result = 'A'
    print('#{} {}'.format(tc,result))

        
        