# Problem : 10개의 수를 입력 받아, 평균값을 출력하는 프로그램
# 소수점 첫째 자리에서 반올림한 정수를 출력한다.
# 각 수는 0 이상 10000 이하의 정수이다.

test_cnt = int(input())
avg_list = [0]*test_cnt

for i in range(test_cnt) :
    sum = 0
    num_list = list(map(int,input().split()))
    for k in num_list :
        sum += k
    avg_list[i] = round(sum/len(num_list))

for i in range(0,test_cnt) :
    print('#{} {}'.format(i+1,avg_list[i]))
