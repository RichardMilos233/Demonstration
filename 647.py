# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# take out the first char, palindromic substrings of s include 
# palindromic substrings of s[1:] and palindromic substrings that incluede the first char


class Solution:
    def __init__(self):
        self.dp = {
            '': True
        }
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s[i: j+1]):
                    count += 1
        return count
    def isPalindrome(self, s):
        if s in self.dp:
            return self.dp[s]
        else:
            r = s[0] == s[-1] and self.isPalindrome(s[1:-1])
            self.dp[s] = r
            return r
  
s = 'abc'
s = 'aaa'

solution = Solution()
ans = solution.countSubstrings(s)
print(ans)