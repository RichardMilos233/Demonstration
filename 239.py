# You are given an array of integers nums, 
# there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        r = []
        for i, n in enumerate(nums):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            
            if i >= k-1:
                r.append(nums[dq[0]])
        return r

nums = [1,3,-1,-3,5,3,6,7]
k = 3


solution = Solution()
ans = solution.maxSlidingWindow(nums, k)
print(ans)