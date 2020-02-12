# Problem[1002] : 터렛
import math

test_cnt = int(input())
result_list = [0]*test_cnt

for i in range(test_cnt):
    result = 0
    num_list = list(map(int,input().split()))
    dist = math.sqrt((num_list[3] - num_list[0])**2 + (num_list[4]-num_list[1])**2)
    r1 = num_list[2]
    r2 = num_list[5]
    if dist == 0 :
        if(r1 == r2) :
            result = -1
        else :
            result = 0
    else :
        if (r1 + r2 == dist) :
            result = 1
        elif (abs(r1-r2) == dist):
            result = 1
        elif (r1 + r2 < dist) :
            result = 0
        elif (abs(r1-r2) > dist) :
            result = 0
        else :
            result = 2
    result_list[i] = result

for i in range(test_cnt) :
    print(result_list[i])     