# Problem : 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
# 각 수는 0 이상 10000 이하의 정수이다.


test_cnt = int(input())
result_list = [0]*test_cnt

for i in range(test_cnt) :
    result = ''
    num_list = list(map(int,input().split()))
    if(len(num_list) > 2):
        print("2개의 수만 입력해주세요.")
    if (num_list[0] > num_list[1]) :
        result = '>'
    elif (num_list[0] < num_list[1]) :
        result = '<'
    elif (num_list[0] == num_list[1]) :
        result = '='
    result_list[i] = result

for i in range(0,test_cnt) :
    print('#{} {}'.format(i+1,result_list[i])) 