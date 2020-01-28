# Problem [1244] : 최대상금
# 각 테스트 케이스에 대해 최대 6자리 정수형 숫자와 교환 횟수를 입력받는다.

def find_max(string,cnt) :
    max_num = 0
    num_list = list(map(int,string))
    start = 0
    flag = 0
    while True:
        if flag == 0 :
            max_num = max(num_list)
            max_idx = [i for i,val in enumerate(num_list) if val == max_num]
        else :
            temp_list = num_list[start:]
            max_num = max(temp_list)
            max_idx = [j for j,value in enumerate(num_list) if value == max_num]
        if max_idx[-1] == start :
            start += 1
            temp_list = num_list[start:]
            max_num = max(temp_list)
            max_idx = [k for k,v in enumerate(num_list) if v == max_num]
        idx = max_idx.pop(-1)
        temp = num_list[idx]
        num_list[idx] = num_list[start]
        num_list[start] = temp
        flag = 1
        start += 1
        cnt -= 1
        if cnt == 0 :
            return num_list      

test_cnt = int(input())
for test in range(1,test_cnt+1) :
    numbers, change_cnt = input().split()
    cnt = int(change_cnt)
    result = find_max(numbers,cnt)
    num = ''.join(map(str,result))
    print('#{} {}'.format(test,num))