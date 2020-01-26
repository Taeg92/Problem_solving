# Problem [1209] : Sum
# 2차원 배열의 열의 합, 행의 합, 대각선의 합을 구하기

for __ in range(10):

    n_val = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]

    sum_list = [sum(row) for row in matrix]
    sum_list.extend(sum(column) for column in zip(*matrix))
    sum_list.append(sum(matrix[i][i] for i in range(100)))
    sum_list.append(sum(matrix[i][99-i] for i in range(100)))
    
    print('#{} {}'.format(n_val,max(sum_list)))