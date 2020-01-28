# Problem [1240] : 단순 2진 암호코드
# 총 8개의 숫자로 이루어져 있다.
# 암호 코드의 규칙이 맞으면 암호코드에 포함된 숫자의 합을 출력
# 입력 첫째줄 : 전체 테스트 케이스
# 입력 둘째줄 : 세로의 길이 N, 가로의 길이 M 입력
# 암호 코드 입력

code = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

def serch_code(arr,col,row) :
    result = list()
    for i in range(1,col):
        for j in range(row-7):
            temp = scanner[i][0][j:j+7]
            if temp in code.keys() :
                for cnt in range(8) :
                    pw = scanner[i][0][j+7*cnt:j+7+7*cnt]
                    if pw in code.keys() :
                        result.append(code[pw])
                        if len(result) == 8 :
                            return result
                    else :
                        result.clear()
                        break

def is_Passwordcode(arr) :
    total_sum = 0
    even_list = [arr[idx] for idx in range(len(arr)) if (idx+1)%2 == 0]
    odd_list = [arr[idx] for idx in range(len(arr)) if (idx+1)%2 == 1]
    total_sum = 3*sum(odd_list)+sum(even_list)
    if total_sum % 10 == 0:
        return True
    return False

test_cnt = int(input())
for test in range(1,test_cnt+1):
    result = 0
    pass_code = list()
    col, row = map(int,input().split())
    scanner = [input().split() for _ in range(col)] 
    pass_code = serch_code(scanner,col,row)
    isPassword = is_Passwordcode(pass_code)
    if isPassword == True: 
        result = sum(pass_code)
    elif isPassword == False:
        result = 0
    print('#{} {}'.format(test,result))