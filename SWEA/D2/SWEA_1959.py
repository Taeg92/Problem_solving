# Problem [1959] : 두개의 숫자열
# N개의 숫자로 구성된 두 배열의 곱의 최댓값 구하기
# 더 긴 배열의 양끝을 벗어날 수 없다.


test_cnt = int(input())

for test in range(1,test_cnt + 1) :
    result = 0
    array_size = list(map(int,input().split()))
    array_a = list(map(int,input().split()))
    array_b = list(map(int,input().split()))
    result_list = list()
    if array_size[0] != array_size[1] :
        if len(array_a) > len(array_b) :
            short_array = array_b
            long_array = array_a
        else :
            short_array = array_a
            long_array = array_b
        diff_size = len(long_array)-len(short_array)
        for i in range(diff_size+1) :
            temp = 0
            for j in range(len(short_array)) :
                temp += short_array[j]*long_array[i+j]
            result_list.append(temp)
    else :
        temp = 0
        for k in range(len(array_a)) :
            temp = array_a[k]*array_b[k]
        result_list.append(temp)

    result = max(result_list)
    print('#{} {}'.format(test,result))