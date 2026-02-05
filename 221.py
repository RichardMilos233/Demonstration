# Given an m x n binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.

class Solution:
    def maxArea(self, hist):
        maxArea = 0
        stack = []
        for i, h in enumerate(hist):
            start = i
            while stack and stack[-1][1] > h:
              index, height = stack.pop()
              maxArea = max(maxArea, min(height, i-index)**2)
              start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, min(h, len(hist)-i)**2)
        return maxArea


    def maximalSquare(self, matrix: list[list[str]]) -> int:
        matrix = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        maxArea = self.maxArea(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
            maxArea = max(maxArea, self.maxArea(matrix[i]))
        return maxArea


solution = Solution()

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

matrix = [["1","1"],
          ["1","1"]]

ans = solution.maximalSquare(matrix)
print(ans)