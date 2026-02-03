# Given a string expression of numbers and operators, 
# return all possible results from computing all the different possible ways to group numbers and operators. 
# You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer 
# and the number of different results does not exceed 10^4.
from collections import defaultdict
symbols = ['+', '-', "*"]
dp = defaultdict(set)

def merge(left, right, s):
    result = set()
    for l in left:
        for r in right:
            match s:
                case "+":
                    r = l + r
                case "-":
                    r = l - r
                case "*":
                    r = l * r
            result.add(r)
    return result

merge([1,2,3], [])


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if not any(s in str for s in symbols):
            dp[str].add(int(str))
            return dp[str]
        result = set()
        for i in range(len(expression)):
            s = expression[i]
            if s in symbols:
                left = expression[:i]
                right = expression[i+1:]
                result.update(merge(self.diffWaysToCompute(left), self.diffWaysToCompute(right), s))
        return list(result)


solution = Solution()

# str = "2-1-1"
# ans = solution.diffWaysToCompute(str)
# print(ans)