# Problem[2008] : 당근 문제
# 입력 첫번째 : 테스트 케이스의 수
# 입력 두번째 : 당근의 개수
# 입력 세번째 : 당근의 크기
# 당근이 연속적으로 커질때 당근을 가질 수 있다. 이때 가질 수 있는 당근의 최대 수는?

test_cnt = int(input())
for test in range(1,test_cnt+1):
    carrot_cnt = int(input())
    carrot = list(map(int,input().split()))
    max_cnt = 1
    cnt = 1
    for i in range(len(carrot)-1) :
        if carrot[i] < carrot[i+1] :
            cnt += 1
        else :
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt  
    print('#{} {}'.format(test,max_cnt))