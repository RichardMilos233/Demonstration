# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. 
# A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.


from collections import defaultdict

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        dp = defaultdict(lambda: -1)

        # length of predecessor chain of word, including word
        def f(words, word):
            if dp[word] != -1:
                return dp[word]
            if len(word) == 0:
                dp[word] = 0
                return 0
            r = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in words:
                    r = max(r, f([w for w in words if len(w)<len(new_word)], new_word)+1)
            dp[word] = r
            return r
        
        return max(f([w for w in words if len(w) < len(word)], word) for word in words)
    
        


solution = Solution()


ls = ["a","b","ba","abc","abd","bdca"]
ls = ["abcd","dbqca"]
ls = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

ans = solution.longestStrChain(ls)
print(ans)