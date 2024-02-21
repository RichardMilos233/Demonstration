def IsSubsequence(s,t):
    l=len(t)
    if s=='':
        return True
    else:
        for i in range(l):
            if t[i]==s[0]:
                return IsSubsequence(s[1::],t[i+1::])
        return False
    

