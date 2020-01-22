# Problem [2056] : 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
# 각 수는 1이상 10000이하의 정수이다.

test_cnt =int(input())
for i in range(test_cnt) :
    a, b = input().split()
    print('#{} {} {}'.format((i+1),int(a)//int(b),int(a)%int(b)))
   