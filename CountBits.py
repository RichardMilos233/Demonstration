def countBits(n):
        m=n
        if n==0:
            return [0]
        else:
            remainder=[]
            while int(n/2)!=0:
                remainder.append(n%2)
                n=int(n/2)
            remainder.append(1)
            count=0
            for i in remainder:
                if i==1:
                    count+=1
            return countBits(m-1)+[int(count)]
# def binary(n):
#     remainder=[]
#     while int(n/2)!=0:
#         remainder.append(n%2)
#         n=int(n/2)
#     remainder.append(1)
#     remainder.reverse()
#     binary=''.join(str(i) for i in remainder)
#     return int(binary)
print(countBits(5))