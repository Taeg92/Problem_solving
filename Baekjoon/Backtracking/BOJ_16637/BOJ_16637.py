# Problem [16637] : 괄호 추가하기

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.stdin = open('input.txt')

m = -2**31

def Backtracking(idx,val):
    global m
    if idx == N:
        m = max(m, val)
        return

    if D[idx] == '+':
        Backtracking(idx + 2,int(val) + int(D[idx+1]))

        if idx == N-2:
            return

        n1 = int(D[idx+1])
        operator = D[idx+2]
        n2 = int(D[idx+3])

        if operator == '+':
            Backtracking(idx + 4,int(val) + (n1 + n2))
        elif operator == '-':
            Backtracking(idx + 4, int(val) + (n1 - n2))
        else:
            Backtracking(idx + 4, int(val) + (n1 * n2))       


    elif D[idx] == '-':
        Backtracking(idx + 2, int(val) - int(D[idx+1]))

        if idx == N-2:
            return

        n1 = int(D[idx+1])
        operator = D[idx+2]
        n2 = int(D[idx+3])

        if operator == '+':
            Backtracking(idx + 4,int(val) - (n1 + n2))
        elif operator == '-':
            Backtracking(idx + 4, int(val) - (n1 - n2))
        else:
            Backtracking(idx + 4, int(val) - (n1 * n2))
    
    else:
        Backtracking(idx + 2, int(val) * int(D[idx+1]))

        if idx == N-2:
            return

        n1 = int(D[idx+1])
        operator = D[idx+2]
        n2 = int(D[idx+3])

        if operator == '+':
            Backtracking(idx + 4,int(val) * (n1 + n2))
        elif operator == '-':
            Backtracking(idx + 4, int(val) * (n1 - n2))
        else:
            Backtracking(idx + 4, int(val) * (n1 * n2))




if __name__ == "__main__":
    N = int(input())
    D = input()
    result = list()
    Backtracking(1, int(D[0]))
    print(m)