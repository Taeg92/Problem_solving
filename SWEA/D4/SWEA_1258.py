# Problem [1258] : 행렬찾기

def find_Arr(arr):
    result = list()
    col_size = len(arr)
    row_size = len(arr[0])
    check = [[0]*row_size for _ in range(col_size)]
    c_col = 0
    c_row = 0
    for i in range(col_size):
        for j in range(row_size):
            if check[i][j] == 0 and arr[i][j] != 0:
                c_col = i
                c_row = j
                while 1:
                    c_col += 1
                    if arr[c_col][c_row] == 0:
                        c_col -= 1
                        break
                    if c_col == col_size -1:
                        break  
                while 1:
                    c_row += 1
                    if arr[c_col][c_row] == 0:
                        c_row -= 1
                        break
                    if c_row == row_size -1:
                        break
                for x in range(i,c_col+1):
                    for y in range(j,c_row+1):
                        check[x][y] = 1
                if [c_col-i+1,c_row-j+1] not in result:
                    result.append([c_col-i+1,c_row-j+1])
    return result




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    sorted_data = sorted(find_Arr(data),key = lambda x : (x[0]*x[1],x[0]))
    cnt = len(sorted_data)
    result = list()
    for data in sorted_data:
        result.extend(data)
    print('#{} {} {}'.format(tc,cnt,' '.join(map(str,result))))