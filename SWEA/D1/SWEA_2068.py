# Problem[2068] : 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
# 각 수는 0 이상 10000 이하의 정수이다.

test_cnt = int(input())
result_list = [0]*test_cnt

for i in range(test_cnt) :
    result = 0
    num_list = list(map(int,input().split()))
    for j in num_list :
        result = max(num_list)
    result_list[i] = result

for i in range(test_cnt) :
    print('#{} {}'.format(i+1,result_list[i]))