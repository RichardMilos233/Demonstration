# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c in ['(','[','{']:
                l.append(c)
                continue
            if not l:
                return False
            if c == ')':
                if l[-1] == '(':
                    l.pop()
                    continue
                else:
                    return False
            if c == ']':
                if l[-1] == '[':
                    l.pop()
                    continue
                else:
                    return False
            if c == '}':
                if l[-1] == '{':
                    l.pop()
                    continue
                else:
                    return False
        return not l

solution  = Solution()

s = "()"
s = "()[]{}"
s = "(]"
s = "([])"
s = "([)]"

ans = solution.isValid(s)
print(ans)