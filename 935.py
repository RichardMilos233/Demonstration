# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, 
# or two squares horizontally and one square vertically (with both forming the shape of an L). 
# The possible movements of chess knight are shown in this diagram:

# We have a chess knight and a phone pad as shown below, 
# the knight can only stand on a numeric cell (i.e. blue cell).

# Given an integer n, return how many distinct phone numbers of length n we can dial.

# You are allowed to place the knight on any numeric cell initially 
# and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

# As the answer may be very large, return the answer modulo 109 + 7.

from collections import defaultdict

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        P = 10**9 + 7
        dp = {i: defaultdict(lambda: 1) for i in range(10)}
        for i in range(2, n+1):
            dp[0][i] = dp[4][i-1] + dp[6][i-1]
            dp[1][i] = dp[8][i-1] + dp[6][i-1]
            dp[2][i] = dp[7][i-1] + dp[9][i-1]
            dp[3][i] = dp[4][i-1] + dp[8][i-1]
            dp[4][i] = dp[3][i-1] + dp[9][i-1] + dp[0][i-1]
            dp[5][i] = 0
            dp[6][i] = dp[1][i-1] + dp[7][i-1] + dp[0][i-1]
            dp[7][i] = dp[2][i-1] + dp[6][i-1]
            dp[8][i] = dp[1][i-1] + dp[3][i-1]
            dp[9][i] = dp[2][i-1] + dp[4][i-1]
            for j in range(10):
                dp[j][i] %= P
        return sum(dp[j][n] for j in range(10)) % P
            
solution  = Solution()

n = 3131
ans = solution.knightDialer(n)
print(ans)