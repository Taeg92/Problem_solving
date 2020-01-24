# Problem [1976] 시각 덧셈
# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램.
# 1<= hour <= 12   0 <= minute <=59

def calc_time(time_list) :
    
    hour1 = time_list[0]
    hour2 = time_list[2]
    minute1 = time_list[1]
    minute2 = time_list[3]

    sum_hour = hour1+hour2
    if sum_hour >= 13 :
        sum_hour -= 12
    sum_minute = minute1+minute2
    if sum_minute >= 60 :
        sum_minute -= 60
        sum_hour += 1 

    return (sum_hour,sum_minute)



test_cnt = int(input())
for test in range(1,test_cnt+1) :
    time = list(map(int,input().split()))
    hour, minute = calc_time(time)
    print('#{} {} {}'.format(test, hour, minute))