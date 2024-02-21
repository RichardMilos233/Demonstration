class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=[i for i in word1]
        l2=[i for i in word2]
        result=''
        if len(word1)>=len(word2):
            for i in range(len(word2)):
                result+=str(l1[i])+str(l2[i])
            for i in range(len(word1)-len(word2)):
                result+=str(l1[len(word2)+i])
            return result
        else:
            for i in range(len(word1)):
                result+=str(l1[i])+str(l2[i])
            for i in range(len(word2)-len(word1)):
                result+=str(l2[len(word1)+i])
            return result
        