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

flag = False
def dfs(n):
    global flag
    if n == len(zero):
        flag = True
        for line in sudoku:
            print(' '.join(map(str,line)))
        return
    if flag:
        return
    else:
        x, y = zero[n]
        if find_answer(sudoku,x,y):
            answer_list = find_answer(sudoku,x,y)
            for answer in answer_list:
                sudoku[x][y] = answer
                dfs(n+1)
                sudoku[x][y] = 0
   

sudoku = [list(map(int,input().split())) for _ in range(9)]
zero = find_zero(sudoku)
dfs(0)