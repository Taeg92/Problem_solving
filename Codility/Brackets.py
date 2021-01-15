def solution(S):
    # write your code in Python 3.6

    table = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    stack = list()

    for char in S:
        if char in table:
            stack.append(char)
        else:
            if not stack:
                return 0
            token = stack.pop()
            if char != table[token]:
                return 0

    if stack:
        return 0
    return 1


S = "([)()]"

print(solution(S))
