def solution(S):
    # write your code in Python 3.6
    stack = list()

    for char in S:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return 0

    if stack:
        return 0
    return 1


S = "())"

print(solution(S))
