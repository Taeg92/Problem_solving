class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)
        check = [[0]*len(grid[0]) for _ in range(len(grid))]
        count = 0

        def DFS(x, y):

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if not check[ny][nx] and grid[ny][nx] == "1":
                        check[ny][nx] = 1
                        DFS(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not check[i][j]:
                    check[i][j] = 1
                    DFS(j, i)
                    count += 1
        return count


grid = [["1", "0", "1", "1", "0", "1", "1"]]
# Output: 3

sol = Solution()
print(sol.numIslands(grid))
