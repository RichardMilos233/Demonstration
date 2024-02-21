def MaxVowels(s,k):
        vowels=['a','e','i','o','u']
        n=len(s)
        substr=s[:k]
        result=0
        for i in substr:
            if i in vowels:
                result+=1
        count=result
        for i in range(k,n):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1
            if count>result:
                result=count
        return result


print(MaxVowels("abciiidef",3))
print(MaxVowels("aeiou",2))
print(MaxVowels("leetcode",3))