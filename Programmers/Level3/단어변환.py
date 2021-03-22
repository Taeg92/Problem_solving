from collections import deque


def solution(begin, target, words):

    def go(words, before):
        result = []

        for word in words:
            diff = [1 for x, y in zip(word, before) if x != y]
            if sum(diff) == 1:
                result.append(word)

        return result

    def bfs(begin):
        visited = dict.fromkeys(words, False)

        queue = deque([(begin, 0)])

        while queue:
            cur, depth = queue.popleft()

            if cur == target:
                return depth

            for word in go(words, cur):
                if not visited[word]:
                    queue.append([word, depth + 1])
                    visited[word] = True

        return 0

    answer = bfs(begin)

    return answer


begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
