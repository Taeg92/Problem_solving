class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def check(row, col):
            for i in range(row):
                if board[i] == col or abs(i-row) == abs(board[i]-col):
                    return False
            return True

        def dfs(level, element):
            if level == n:
                result.append(element)
                return
            for i in range(n):
                if check(level, i):
                    board[level] = i
                    dfs(level+1, element+["." * i + "Q" + "." * (n - i - 1)])

        board = [0] * n
        result = []
        dfs(0, [])
        return result


n = 4

sol = Solution()

print(sol.solveNQueens(n))
