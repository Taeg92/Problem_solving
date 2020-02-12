# Problem [1003] : 피보나치 함수
# fibonacci(N) 함수를 호출 했을 때, 0과 1이 몇번 출력했는지 구하는 문제
# 첫째 줄에는 테스트 케이스 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다.  0 <= N <= 40

def fibonacci(n) :

    
    if n == 0 :
        zero_cnt = [1]
        one_cnt = [0]
    elif n == 1 :
        zero_cnt = [0]
        one_cnt = [1]
    else :
        zero_cnt = [1,0]
        one_cnt = [0,1]
        for i in range(2,n+1) :
            zero_cnt.append(zero_cnt[i-1]+zero_cnt[i-2])
            one_cnt.append(one_cnt[i-1]+one_cnt[i-2])
    
    return max(zero_cnt), max(one_cnt)


test_cnt = int(input())
for test in range(test_cnt):
    n = int(input())
    zero_count = 0
    one_count = 0
    zero_count, one_count = fibonacci(n)
    print('{} {}'.format(zero_count,one_count))
    