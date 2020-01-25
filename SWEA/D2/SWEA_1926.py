# Problem [1926] : 간단한 3 6 9 게임
# 3, 6 ,9 가 들어는 부분을 숫자 대신 들어가는 횟수만큼 -를 출력한다.


test_cnt = int(input())
number_list = list()
result_list = list()
for i in range(1,test_cnt+1) :
    number_list.append(str(i))

for num in number_list :
    if '3' in num :
        count = num.count('3') + num.count('6') + num.count('9')
        result_list.append('-'*count)
    elif '6' in num :
        count = num.count('3') + num.count('6') + num.count('9')
        result_list.append('-'*count)
    elif '9' in num :
        count = num.count('3') + num.count('6') + num.count('9')
        result_list.append('-'*count)
    else :
        result_list.append(num) 


string = ' '.join(map(str,result_list))
print(string)