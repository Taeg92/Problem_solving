# Problem [1961] : 숫자 배열 회전
# N x N 행렬이 주어질 때,
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

test_cnt = int(input())

for test in range(1,test_cnt+1):

    size=int(input())
    matrix = [list(input().split()) for i in range(size)]
    result_list=['' for j in range(size)]

    for case in range(3):
        temp_matrix = ['' for k in range(size)]
        for column in range(size):
            for row in range(size):
                temp_matrix[column] += matrix[size-row-1][column]
        matrix=temp_matrix

        for idx in range(size):
            result_list[idx] += temp_matrix[idx] + ' '
    print('#{}'.format(test))
    for line in range(size):
        print(result_list[line])

