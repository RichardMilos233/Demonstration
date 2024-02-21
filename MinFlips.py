def binary(n):
    remainder=[]
    while int(n/2)!=0:
        remainder.append(n%2)
        n=int(n/2)
    remainder.append(1)
    remainder.reverse()
    for i in range(31-len(remainder)):
        remainder=[0]+remainder
    return remainder


def MinFlips(a,b,c):
        abin=binary(a)
        bbin=binary(b)
        cbin=binary(c)
        count=0
        for i in range(31):
            if cbin[i]==0:
                count+=abin[i]+bbin[i]
            else:
                count+=int(abin[i]+bbin[i]==0)
        return count

print(MinFlips(1,2,3))
