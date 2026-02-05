# Given a rows x cols binary matrix filled with 0's and 1's, 
# find the largest rectangle containing only 1's and return its area.

class Solution:
    # from 84
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea
    
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        matrix = [[int(matrix[i][j]) for j in range(len(matrix[0]))]for i in range(len(matrix))]
        maxArea = self.largestRectangleArea(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
            hist = matrix[i]
            maxArea = max(maxArea, self.largestRectangleArea(hist))
        return maxArea




matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

ans = Solution().maximalRectangle(matrix)
print(ans)