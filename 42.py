# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left_max, right_max = [0]*n, [0]*n
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            h = height[i]
            left_max[i] = max(h, left_max[i-1])

            h = height[n-i-1]
            right_max[n-i-1] = max(h, right_max[n-i])
        return sum(min(left_max[i], right_max[i])-height[i] for i in range(n))

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

solution = Solution()

ans = solution.trap(height)
print(ans)