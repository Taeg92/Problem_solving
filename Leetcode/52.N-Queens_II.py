class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(row, col):
            for i in range(row):
                if board[i] == col or abs(i-row) == abs(board[i]-col):
                    return False
            return True

        def dfs(level):
            if level == n:
                self.result += 1
                return
            for i in range(n):
                if check(level, i):
                    board[level] = i
                    dfs(level + 1)

        board = [0] * n
        self.result = 0
        dfs(0)
        return self.result


n = 4

sol = Solution()

print(sol.totalNQueens(n))
