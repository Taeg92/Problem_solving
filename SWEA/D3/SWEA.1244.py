# # Problem [1244] : 최대상금
# # 각 테스트 케이스에 대해 최대 6자리 정수형 숫자와 교환 횟수를 입력받는다.

def find_max(arr,cnt) :
    original = list(sorted(arr[0]))[::-1]
    original_max = int(''.join(map(str,original)))
    temp = list()
    while cnt > 0 :
        for array in arr:
            for i in range(len(array)-1):
                for j in range(i+1,len(array)):
                    copy_arr = array[:]
                    copy_arr[i] , copy_arr[j] = copy_arr[j], copy_arr[i]
                    if copy_arr not in temp :
                        temp.append(copy_arr[:])
        arr.extend(temp)
        cnt -= 1
        
        max_num = max([int(''.join(map(str,lst))) for lst in arr])
        
        if max_num == original_max and cnt != 0:
            max_list = original
            for _ in range(cnt):
                max_list[-1], max_list[-2] = max_list[-2], max_list[-1]
            return int(''.join(map(str,max_list)))
    
    my_result = [int(''.join(map(str,lst))) for lst in arr]
    return max(my_result)
        


test_cnt = int(input())
for test in range(1,test_cnt+1) :
    numbers, change_cnt = input().split()
    cnt = int(change_cnt)
    result = find_max([list(numbers)],cnt)
    print('#{} {}'.format(test,result))
