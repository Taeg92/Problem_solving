# Problem [4831] :전기버스
# 한번 충전으로 최대한 갈 수 있는 정류장 수 K , 종점 N번, 충전기 설치 수 N
# N개의 정류장 번호


test_cnt = int(input())
for test in range(1,test_cnt+1):
    k_val, n_val, m_val = map(int, input().split())
    arr = list(map(int,input().split()))
    min_stop = 0
    start = 0
    stop_idx = 0
    while 1:
        stop_idx = start + k_val
        while stop_idx not in arr :
            stop_idx -= 1
        if stop_idx == start :
            min_stop = 0
            break
        start = stop_idx
        min_stop += 1
        if stop_idx + k_val >= n_val:
            break
    print('#{} {}'.format(test,min_stop))
            
        
        