def findmax(l):
    length=len(l)
    m=l[0]
    for i in range(length):
        if l[i]>m:
            m=l[i]
    return m





def KidsWithCandies(candies,extraCandies):
    n=len(candies)
    maxcandies=findmax(candies)
    result=[]
    for i in range (n):
        kidwithextra=candies[i]+extraCandies
        result+=[kidwithextra>=maxcandies]
    return result

print(KidsWithCandies([12,1,12],10))