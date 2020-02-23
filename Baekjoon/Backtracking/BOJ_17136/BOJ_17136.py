# Problem [17136] : 색종이 붙이기

import sys
sys.stdin = open('input.txt')


def Backtracking(x,y,size,cnt):
    
    for i in range(x,x + size):
        for j in range(y, y + size):
            if not check[i][j]:
                D[i][j] = 0

    # 문제 1: 돌리는 방법 
    # 해결 방법 1 => deep.copy => 할때마다 복사 => 시간 초과 날수도?
    # 바꾸기 전 상황 deep.copy 바꾸고 다시 전상황으로 돌리고 다음 색종이 출발
    # 고민 좀더 해보기


if __name__ == "__main__":
    D = [list(map(int,input().split())) for _ in range(10)]
    check = [[0]*10 for _ in range(10)]
    axis = [[i,j] for i in range(10) for j in range(10) if D[i][j] == 1]
    print(axis)