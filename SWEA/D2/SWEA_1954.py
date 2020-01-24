# Problem [1954] : 달팽이 숫자
# 달팽이의 크기느 N은 1이상 10 이하의 정수이다.
# 가장 첫 줄에는 테스트 케이스 개수 T
# 각 테스트 케이스에는 N이 주어진다.

test_cnt = int(input())

for test in range(1,test_cnt+1) :
    size = int(input())
    n_matrix = [[0]*size for __ in range(size)]
    start = 1
    pos = 1
    row = 0
    column = -1
    count = size
    while count > 0 :
        for __ in range(count) :
            column += pos
            n_matrix[row][column] = start
            start += 1
        count -= 1
        #if count == 0:
        #    break
        for __ in range(count) :
            row += pos
            n_matrix[row][column] = start
            start += 1 
        pos *= -1

    print('#{}'.format(test))
    for i in range(size) :
        for j in range(size) :
            print(n_matrix[i][j],end = ' ')
        print('')

