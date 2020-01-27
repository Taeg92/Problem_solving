# Problem [1217] : 거듭 제곱
# 숫자 N,M 이 주어질 때, N의 M 거듭 제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보기.
# 첫 줄에는 테스트 케이스 번호, 그 다음 줄에는 두 개의 숫자 입력.

def Power(n_val,m_val) :

    if m_val == 1 :
        return n_val
    else :
        return n_val*Power(n_val,m_val-1)

for test in range(10) :
    test_case = input()
    n_val, m_val = map(int,input().split())
    result = Power(n_val,m_val)
    print('#{} {}'.format(test_case,result))