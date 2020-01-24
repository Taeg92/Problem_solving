# Problem [1948] : 날짜 계산기
# 입력 : 월 일로 이루어진 날짜 2개
# 두 번째 날짜가 첫 번째 날짜의 몇칠째 인지 출력
# 두 번째 날짜 > 첫 번쨰 날짜

calendar = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

test_cnt = int(input())

for test in range(1,test_cnt+1) :
    result = 0
    calc_date = list(map(int,input().split()))
    month1 = calc_date[0]
    date1 = calc_date[1]
    month2 = calc_date[2]
    date2 = calc_date[3]
    date_sum1 = 0
    date_sum2 = 0
    if month1 == month2:
        result = date2 - date1 + 1
    else : 
        for i in range(1,month1) :
            date_sum1 += calendar[i]
        for i in range(1,month2) :
            date_sum2 += calendar[i]
        result = (date_sum2+date2) - (date_sum1 + date1) + 1
    print('#{} {}'.format(test,result))