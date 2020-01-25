# Problem [1984] : 중간 평균값 구하기
# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램
# 소수점 첫째 자리에서 반올림한 정수를 출력


test_cnt = int(input())

for test in range(1,test_cnt+1) :

    result_avg = 0
    sum = 0
    result = 0

    numbers = list(map(int,input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    
    for number in numbers :
        sum += number

    result_avg = sum/len(numbers)
    result = round(result_avg)

    print('#{} {}'.format(test,result))