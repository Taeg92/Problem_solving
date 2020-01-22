# Problem : 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

def doulbe_Num(n) :
    if n > 1 :
        return doulbe_Num(n-1)*2
    else :
        return 1

num = int(input())
num_list = list()
for i in range(1,num+2):
    num_list.append(doulbe_Num(i))

string = ' '.join(map(str,num_list))
print(string)

