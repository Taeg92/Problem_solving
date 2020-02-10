# Problem [10157] : 자리배정

C, R = map(int,input().split())
K = int(input())
n_matrix = [[0]*C for __ in range(R)]
start = 1
pos = 1
col_count = R
row_count = C
col = R
row = 0

while col_count > 0 :
    for __ in range(col_count) :
        col -= pos
        n_matrix[col][row] = start
        if start == K:
            x = row + 1
            y = R - col
        start += 1
    row_count -= 1
    for __ in range(row_count) :
        row += pos
        n_matrix[col][row] = start
        if start == K:
            x = row + 1
            y = R - col
        start += 1
    col_count -= 1
    pos *= -1

if start < K+1:
    print('0')
else:
    print('{} {}'.format(x,y))