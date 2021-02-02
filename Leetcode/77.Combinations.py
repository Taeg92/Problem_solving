class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result


n = 4
k = 2
# Output = [
#     [2, 4],
#     [3, 4],
#     [2, 3],
#     [1, 2],
#     [1, 3],
#     [1, 4],
# ]

sol = Solution()

print(sol.combine(n, k))
