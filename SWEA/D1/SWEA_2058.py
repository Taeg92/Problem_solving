# Problem[2058] : 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
# 자연수 N은 1부터 9999까지의 자연수이다.

num = input()
sum = 0
for i in num :
    sum += int(i)
print(sum)