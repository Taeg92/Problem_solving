# Problem [10872] : 팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다. 이때 N!을 재귀로 구현한 프로그램을 작성하시오.

def factorial(n):

    if n < 2:
        return 1
    else :
        return n*factorial(n-1)

n_val = int(input())
print(factorial(n_val))