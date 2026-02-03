# Given an integer n, 
# return the number of ways you can write n as the sum of consecutive positive integers.

# length is odd: 2n = (2 * mid) * length, requirement: (2 * mid) > length
# length is even: 2n = (mid1 + mid2) * length, requirement: (mid1 + mid2) > length
# find all odd divisors n <==> all odd divisors of n
# factor out n

# from sympy import factorint

def factorint(n):
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        factors = factorint(n)
        if 2 in factors:
            factors.pop(2)
        if not factors:
            return 1
        s = 1
        for key in factors:
            s *= factors[key] + 1
        return s


solution = Solution()

n=1
ans = solution.consecutiveNumbersSum(n)

print(ans)
        