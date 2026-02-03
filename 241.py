# Given a string expression of numbers and operators, 
# return all possible results from computing all the different possible ways to group numbers and operators. 
# You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer 
# and the number of different results does not exceed 10^4.
from collections import defaultdict
symbols = ['+', '-', "*"]
dp = defaultdict(list)

def merge(left, right, s):
    result = []
    for l in left:
        for r in right:
            match s:
                case "+":
                    r = l + r
                case "-":
                    r = l - r
                case "*":
                    r = l * r
            result.append(r)
    return result



class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if not any(s in expression for s in symbols):
            dp[expression] = [int(expression)]
            return dp[expression]
        if expression in dp:
            return dp[expression]
        result = []
        for i in range(len(expression)):
            s = expression[i]
            if s in symbols:
                left = expression[:i]
                right = expression[i+1:]
                result += merge(self.diffWaysToCompute(left), self.diffWaysToCompute(right), s)
        dp[expression] = result
        return dp[expression]


solution = Solution()

s = "2-1-1"
# s = "2-1"
s = "2*3-4*5"
ans = solution.diffWaysToCompute(s)
print(ans)