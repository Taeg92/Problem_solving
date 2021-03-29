def solution(numbers, target):

    def dfs(s, val):
        cnt = 0
        if s == len(numbers):
            if val == target:
                return 1
        else:
            cnt += dfs(s + 1, val + numbers[s])
            cnt += dfs(s + 1, val - numbers[s])

        return cnt

    answer = dfs(0, 0)

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))
