# Proble [1945] : 간단한 소인수 분해
# N은 2이상 10000000 이하이다.

def find_exponent(base,num) :
    cnt = 1
    while True :
        if num % base**cnt != 0 :
            break
        cnt += 1
    return cnt-1

test_cnt = int(input())
n_list = [2,3,5,7,11]

for count in range(1,test_cnt+1):
    result = list()
    test_num = int(input())
    for base in n_list:
        result.append(find_exponent(base,test_num))
    string = ' '.join(map(str,result))
    print('#{} {}'.format(count,string))

