def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]

    A.sort()

    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        elif A[i] != A[i+1]:
            return A[i]


A = [9, 3, 9, 3, 9, 7, 9]

print(solution(A))
