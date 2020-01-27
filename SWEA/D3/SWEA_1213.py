# Problem [1213] : String
# 주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램

test_cnt = 10
for test in range(test_cnt) :
    result = 0
    n_val = int(input())
    serch_string = input()
    string = input()
    result = string.count(serch_string)
    print('#{} {}'.format(n_val,result))