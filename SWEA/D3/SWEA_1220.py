# Proble [1220] : Magnetic
# 100X100 테이블 위에 자성체들이 놓여져있따.
# 첫째 줄에는 정사각형 테이블의 한변의 길이가 입력, 그 다음 줄에는 테스트 케이스
# 1 : N극 , 2 : S극

for test in range(1,11) :
    result = 0
    size = int(input())
    matrix = [list(map(int,input().split())) for _ in range(size)] 
    row_list = [i for i in zip(*matrix)]
    flag = 0
    for row in row_list :
        idx = 0
        while idx != 100 :
            if row[idx] == 1 :
                flag = 1
            if row[idx] == 2 and flag == 1 :
                flag = 0
                result += 1
            idx += 1
        flag = 0
    print('#{} {}'.format(test,result))