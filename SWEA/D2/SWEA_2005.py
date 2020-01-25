# Problem [2005] : 파스칼의 삼각형 크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# 첫번쨰 줄은 항상 숫자 1, 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성.

def pascal_tri(n) :
    output_Arr = list()
    if n == 1 :
        return [1]
    elif n == 2 :
        return [1,1]
    else :
        output_Arr = [1]
        for i in range(len(pascal_tri(n-1))-1) :
            output_Arr.append(pascal_tri(n-1)[i]+pascal_tri(n-1)[i+1])
        output_Arr.append(1)
    
    return output_Arr

test_cnt = int(input())
for test in range(1,test_cnt+1) :
    n_val = int(input())
    print('#{}'.format(test))
    for i in range(1,n_val+1) :
        print(' '.join(map(str,pascal_tri(i))))
