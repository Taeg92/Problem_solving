# Problem [1284] : 수도 요금 경쟁
# 입력 : P, Q, R, S, W
# A사: PW
# B사: Q+(W-R)S

test_cnt = int(input())

for test in range(test_cnt):
    values = list(map(int,input().split()))
    p_value = values[0]
    q_value = values[1]
    r_value = values[2]
    s_value = values[3]
    w_value = values[4]
    min_price = 0
    if w_value< r_value :
        min_price = (min(p_value*w_value,q_value))
    else :
        min_price = (min((q_value+(w_value-r_value)*s_value),p_value*w_value))
    print('#{} {}'.format(test+1,min_price))    