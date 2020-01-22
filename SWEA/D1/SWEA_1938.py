#problem [1938] : 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

num = list(map(int,input().split()))

print(num[0]+num[1])
print(num[0]-num[1])
print(num[0]*num[1])
print(num[0]//num[1])