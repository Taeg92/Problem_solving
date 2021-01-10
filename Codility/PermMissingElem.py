def solution(A):
    # write your code in Python 3.6
    total = sum(range(len(A)+2))

    return total - sum(A)


A = [2, 3, 1, 5]

print(solution(A))
