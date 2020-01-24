# Problem [1966] : 숫자를 정려랗라
# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

def counting_sort(arr) :

    max_num = max(arr)
    count_array = [0]*(max_num+1)

    for i in arr :
        count_array[i] += 1
    
    for j in range(max_num) :
        count_array[j+1] += count_array[j]
    
    result_array = [0]*len(arr)

    for k in arr :
        result_array[count_array[k]-1] = k
        count_array[k] -= 1
    
    return result_array
    
test_cnt = int(input())

for test in range(1,test_cnt+1):
    size = int(input())
    result = ''
    result_list = list()
    numbers = list(map(int,input().split()))
    result_list = counting_sort(numbers)
    result = ' '.join(map(str,result_list))
    print('#{} {}'.format(test,result))