# Problem [2043] : 서랍의 비밀번호
# 비밀번호 P는 000부터 999까지 번호 중의 하나이다.
# 주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
# P가 123이고 번호 K가 100일때 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
# P와 K가 주어진다 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.


test_input = list(map(int,input().split()))

p_Num = test_input[0]
k_Num = test_input[1]

if p_Num > k_Num :
    print('{}'.format(p_Num - k_Num + 1))
elif p_Num == k_Num:
    print('0')
else :
    print('{}'.format(1000-k_Num+p_Num))