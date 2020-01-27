# Problem [1213] : 회문 1
# 주어진 8X8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제
# 각 케이스마다 회문의 길이와 평면 글자판을 입력받음.


for test in range(1,11) :
    result = 0
    len_pal = int(input())
    row = [''.join(input().split()) for _ in range(8)]
    col = [''.join(i) for i in zip(*row)]
    row.extend(col)
    for string in row :
        for idx in range(len(string)-len_pal+1) :
            string1 = list(string[idx:idx+len_pal])
            string2 = list(reversed(string1))
            if string1 == string2 :
                result += 1
    print('#{} {}'.format(test,result))