def ReverseVowels(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    target=[]
    str2lst=[]
    n=len(s)
    for i in s:
        str2lst+=[i]
        if i in vowels:
            target+=[i]
    reversetarget=target[-1::-1]
    count=0
    for i in range(n):
        if s[i] in vowels:
            str2lst[i]=reversetarget[count]
            count+=1
    return ''.join(str2lst)

print(ReverseVowels('motherfucker'))
