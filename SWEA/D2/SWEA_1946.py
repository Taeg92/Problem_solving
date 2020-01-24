# Proble [1946] 간단한 압축 풀기
# 원본 문서의 너비가 10인 여러 줄의 문자열로 이루어져 있다.
# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.
# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다.
# 주어진 알파벳은 A~Z 대문자
# N 은 1이상 10이하
# K 는 1이상 20이하


test_cnt = int(input())

for test in range(1,test_cnt+1) :
    result_list = list()
    alpha_cnt = int(input())
    result = ''
    for times in range(alpha_cnt) :
        zip_list = list(input().split())
        result += zip_list[0]*int(zip_list[1])

    print('#{}'.format(test))
    for index,char in enumerate(result,start=1) :
        print(char,end ='')
        if index % 10 == 0:
            print('')
    print('')