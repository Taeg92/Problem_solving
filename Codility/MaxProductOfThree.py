def solution(A):
    # write your code in Python 3.6
    A.sort()
    val1 = A[0] * A[1] * A[-1]
    val2 = A[-1] * A[-2] * A[-3]
    return max(val1, val2)


A = [-3, 1, 2, -2, 5, 6]

print(solution(A))
