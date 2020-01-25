# Problem [1986] : 지그재그 숫자
# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

def calc_Zigzag(n) :
    if n == 1 :
        return 1
    else :
        if n % 2 == 0 :
            return calc_Zigzag(n-1) - n
        else :
            return calc_Zigzag(n-1) + n
        

test_num = int(input())

for test in range(1,test_num+1) :
    
    n_val = int(input())
    result = calc_Zigzag(n_val)
    print('#{} {}'.format(test,result))