# Problem [2578] : 빙고


def is_Bingo(arr):
    # 가로 세로 +대각 -대각
    cnt = 0
    row_arr = [list(i) for i in zip(*arr)]
    plus_diagonal = [arr[i][i] for i in range(len(arr))]
    minus_diagonal =[arr[i][4-i] for i in range(len(arr))]
    
    if plus_diagonal == [0,0,0,0,0]:
        cnt += 1
    if minus_diagonal == [0,0,0,0,0]:
        cnt += 1
    for i in range(5):
        if arr[i] == [0,0,0,0,0]:
            cnt += 1
            if cnt == 3:
                return True
    for i in range(5):
        if row_arr[i] == [0,0,0,0,0]:
            cnt += 1
            if cnt == 3:
                return True

    
def check_n(arr,n):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                return i,j

def bingo(data,answer):
    cnt = 0
    for i in range(5):
        for j in range(5):
            cnt += 1
            x, y = check_n(data,answer[i][j])
            data[x][y] = 0
            if is_Bingo(data):
                return cnt

data = [list(map(int,input().split())) for _ in range(5)]
answer = [list(map(int,input().split())) for _ in range(5)]

result = bingo(data,answer)
print(result)