# Proble [1940] : 가랏! RC카!
# Command 종류 : 가속, 감속, 현재 속도 유지
# 가속도의 종류 : 1,2
# 입력(N) : 2 <= N <= 30

test_cnt = int(input())
for count in range(1,test_cnt+1):
    velocity = 0
    dist = 0
    command_num = int(input())
    for command_count in range(command_num):

        # value_list = [command, accelration]
        value_list = list(map(int,input().split()))
        if value_list[0] == 0 :
            dist += velocity
        elif value_list[0] == 1 :
            velocity += value_list[1]
            dist += velocity
        else :
            velocity -= value_list[1]
            if velocity <= 0:
                velocity = 0
            dist += velocity
    print('#{} {}'.format(count,dist))
