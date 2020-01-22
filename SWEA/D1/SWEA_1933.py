# Problem [1933] : 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.


num = int(input())
num_list = list()
for i in range(1,num+1) :
    if(num % i == 0) :
        num_list.append(i)

string = ' '.join(map(str,num_list))
print(string)
        