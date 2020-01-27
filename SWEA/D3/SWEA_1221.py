# Problem [1221] : GNS
# ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN 순으로 출력하기.
# 첫 줄에는 테스트 케이스 개수
# 그 다음 줄에는 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

n_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

test_cnt = int(input())
for test in range(test_cnt):
    test_case, case_length = input().split()
    num_list = list(input().split())
    result_list = list()
    for i in n_list :
        for _ in range(num_list.count(i)):
            result_list.append(i)
    result = ' '.join(map(str,result_list))
    print(test_case)
    print(result)