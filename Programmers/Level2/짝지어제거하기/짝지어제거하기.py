def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack or stack[len(stack) - 1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()

    return 0 if stack else 1


s = "baabaa"
print(solution(s))
