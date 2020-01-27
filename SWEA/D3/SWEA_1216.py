# Problem [1213] : 회문 2
# 주어진 8X8 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문을 구하는 문제
# 각 케이스마다 평면 글자판을 입력 받음.


for test in range(10) :
    test_num = int(input())
    row = [''.join(input().split()) for _ in range(100)]
    col = [''.join(i) for i in zip(*row)]
    row.extend(col)
    len_pal = 1
    max_string = list()
    max_len = 0
    for string in row :
        for start in range(100) :
            for length in range(101-start) :
                my_string = list(string[start:start+length])
                rev_string = list(reversed(my_string))
                if my_string == rev_string :
                    if max_len < len(my_string) :
                        max_string = my_string
                        max_len = len(max_string)
    print('#{} {}'.format(test_num,max_len))