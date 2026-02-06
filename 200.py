# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def dfs(self, i, j, visited, grid):
        m, n = len(grid), len(grid[0])
        neighbors = []
        if i-1 >= 0:
            neighbors.append((i-1, j))
        if i+1 < m:
            neighbors.append((i+1, j))
        if j-1 >= 0:
            neighbors.append((i, j-1))
        if j+1 < n:
            neighbors.append((i, j+1))
        for x, y in neighbors:
            if visited[x][y]:
                continue
            else:
                visited[x][y] = True
                if grid[x][y] == "1":
                    self.dfs(x, y, visited, grid)

    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, visited, grid)
        return count

solution = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


ans = solution.numIslands(grid)
print(ans)