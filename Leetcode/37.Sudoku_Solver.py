class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def check(row, col):
            val = board[row][col]
            board[row][col] = -1

            for i in range(9):
                if board[row][i] == val:
                    return False

            for i in range(9):
                if board[i][col] == val:
                    return False

            for i in range(3):
                for j in range(3):
                    x = int(row / 3) * 3 + i
                    y = int(col / 3) * 3 + j
                    if board[x][y] == val:
                        return False

            board[row][col] = val

            return True

        def dfs(board):

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for ans in answer_table:
                            board[i][j] = ans
                            if check(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        answer_table = '123456789'
        dfs(board)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

sol = Solution()

print(sol.solveSudoku(board))
