# Problem [1974] : 스도쿠 검증
# 가로 9칸, 세로 9칸 부터 9까지의 숫자

def check_Sudoku(arr):
    for i in range(9):
        sum_row = 0
        sum_column = 0
        for j in range(9):
            sum_row += arr[i][j]
            sum_column += arr[j][i]
        if sum_row != 45 or sum_column != 45:
            return 0
    for start_point_width in range(0, 9, 3):
        for start_point_height in range(0, 9, 3):
            sum_rec = 0
            for rec_width in range (3):
                for rec_height in range(3):
                    sum_rec += arr[start_point_width+rec_width][start_point_height+rec_height]
            if sum_rec != 45:
                return 0
    return 1

test_cnt = int(input())   
for test in range(1, test_cnt+1):
    matrix = [list(map(int, input().split())) for __ in range(9)]
    result = check_Sudoku(matrix)
    print('#{} {}'.format(test,result))