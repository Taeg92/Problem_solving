# Problem [2580] : 스도쿠

def find_answer(arr,i,j):
    data = range(1,10)
    temp = set()
    # 행 검사
    for row in range(len(arr)):
        temp.add(arr[i][row])
    # 열 검사
    for col in range(len(arr)):
        temp.add(arr[col][j])
    # 작은 네모 검사
    s_col = 3*(i//3)
    s_row = 3*(j//3)
    for col in range(s_col,s_col+3):
        for row in range(s_row,s_row+3):
            temp.add(arr[col][row])
    
    answer = set(data)-temp
    return list(answer)
    
def find_zero(sudoku) :
     result = [[i,j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]
     return result


def solve_sudoku(sudoku,zero):
    for i in range(len(zero)):
        if len(zero) == 0:
            return sudoku
        else:
            if len(find_answer(sudoku,zero[i][0],zero[i][1])) == 1:
                x, y = zero.pop(i)
                sudoku[x][y] = find_answer(sudoku,x,y)[0]
                solve_sudoku(sudoku,zero)       

sudoku = [list(map(int,input().split())) for _ in range(9)]
zero = find_zero(sudoku)
result = solve_sudoku(sudoku,zero)

for line in result:
    print(' '.join(map(str,line)))