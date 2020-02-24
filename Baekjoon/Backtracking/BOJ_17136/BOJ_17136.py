# Problem [17136] : 색종이 붙이기

import sys
sys.stdin = open('input.txt')

m = sys.maxsize

def chance_paper(x,y,size,val):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if 0 <= i < 10 and 0 <= j < 10:
                D[i][j] = val


def check_paper(x,y,size):
    for i in range(x,x+size):
        if i >= 10:
            return False
        for j in range(y,y+size):
            if j >= 10:
                return False
        
            else:
                if D[i][j] == 0:
                    return False
    return True


def Backtracking(start,cnt):
    global m
    global flag
    if cnt >= m:
        return
    if start == N:
        flag = 1
        m = min(m,cnt)
        return

    x, y = axis[start]
    if D[x][y]:
        for i in range(5):
            if paper[i]:
                if check_paper(x,y,5-i):
                    chance_paper(x,y,5-i,0)
                    paper[i] -= 1
                    Backtracking(start+1,cnt+1)
                    paper[i] += 1
                    chance_paper(x,y,5-i,1)
    else:
        Backtracking(start+1,cnt)
                

if __name__ == "__main__":
    D = [list(map(int,input().split())) for _ in range(10)]
    check = [[0]*10 for _ in range(10)]
    axis = [[i,j] for i in range(10) for j in range(10) if D[i][j] == 1]
    paper = [5, 5, 5, 5, 5]
    N = len(axis)
    flag = 0
    Backtracking(0,0)
    if flag == 0:
        print(-1)
    if flag == 1:
        print(m)