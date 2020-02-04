# Problem [4843] : 특별한 정렬

import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    reversed_n = list(sorted(numbers,reverse=True))
    flag = 0
    result = list()
    while len(reversed_n) != 0 :
        if flag == 0 :
            result.append(reversed_n.pop(0))
            flag = 1
        if flag == 1 :
            result.append(reversed_n.pop(-1))
            flag = 0
    print('#{} {}'.format(tc,' '.join(map(str,result[:10]))))
