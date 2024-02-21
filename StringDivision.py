def factors(a):
    lst=[]
    for i in range(1,a//2+1):
        if a%i==0:
            lst.append(i)
    lst.append(a)
    return lst

def commonfactors(a,b):
    lst=[]
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            lst.append(i)
    return lst

def divide(a,b):
    d=''
    if len(a)>len(b):
        return False
    else:
        while len(d)<len(b):
            d+=a
        if d==b:
            return True
        else:
            return False

def gcdOfStrings(str1,str2):
    cfl=commonfactors(len(str1),len(str2))
    result=''
    if cfl==[]:
        return result
    else:
        for i in cfl:
            b=str1[0:i]
            if divide(b,str2) and divide(b,str1):
                result=b
        return result

print(commonfactors(2,8))
print(gcdOfStrings('ab','ababab'))




