# Problem [4008] : [모의 SW 역량 테스트] 숫자 만들기

import sys
sys.stdin = open('input.txt')

def Backtracking(n, v):
    global min_val, max_val
    if n == N:
        min_val = min(min_val, v)
        max_val = max(max_val, v)

    for i in range(4):
        if O[i]:
            O[i] -= 1
            if i == 0:
                Backtracking(n+1, v + D[n])
            elif i == 1:
                Backtracking(n+1, v - D[n])
            elif i == 2:
                Backtracking(n+1, v * D[n])
            else:
                if v < 0:
                    Backtracking(n+1, -(abs(v)//D[n]))
                else:
                    Backtracking(n+1, v // D[n])
            O[i] += 1
 
if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        min_val = 100000000
        max_val = -100000000
        N = int(input())
        O = list(map(int,input().split()))
        D = list(map(int,input().split()))
        Backtracking(1,D[0])
        result = max_val - min_val
        print('#{} {}'.format(tc,result))