# Problem[2072] : 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램
# 각 수는 0 이상 10000 이하의 정수이다.

test_cnt = int(input())
sum_list = [0]*test_cnt

for i in range(test_cnt) :
    sum = 0
    num_list = list(map(int,input().split()))
    for k in num_list :
        if k % 2:
            sum += k
    sum_list[i] = sum

for i in range(0,test_cnt) :
    print('#{} {}'.format(i+1,sum_list[i]))
