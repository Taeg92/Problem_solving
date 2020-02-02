# Problem [1860] : 진기의 최고급 붕어빵
# 첫 번째 줄 : 테스트 케이스 T
# 두 번째 줄 : N(사람수),M,K => M(초동안) K(개의) 붕어빵을 만듬
# 세 번째 줄 : N명의 사람이 도착하는 시간

test_cnt = int(input())
for test in range(1,test_cnt+1):
    n_val, m_val, k_val = map(int, input().split())
    people_idx = sorted(list(map(int,input().split())))
    max_time = max(people_idx)
    bread = 0
    eat_bread = 0
    last_time = 0
    result = 'Possible'
    for time in people_idx:
        eat_bread += 1
        bread = k_val*(time//m_val) - eat_bread
        last_time = time
        if bread == -1 :
            result = 'Impossible'
            break
    print('#{} {}'.format(test,result))