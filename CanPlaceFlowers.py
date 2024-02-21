def CanPlaceFlowers(flowerbed,n):
    flowerlength=len(flowerbed)
    if flowerbed==[1]:
        m=0
    elif flowerbed==[0]:
        m=1
    else:
        if flowerbed[0]==1 or (flowerbed[0]==0 and flowerbed[1]==1):
            m=0
            print(m)
        else:
            flowerbed[0]=1
            m=1
        for i in range(1,flowerlength-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                m+=1
        if flowerbed[-2]==0 and flowerbed[-1]==0:
            flowerbed[-1]=1
            m+=1
    return m>=n



print(CanPlaceFlowers([0,0],2))
