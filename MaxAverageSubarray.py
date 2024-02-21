def FindMaxAverage(nums, k):
        # n=len(nums)
        # avg=round(sum(nums)/n)
        # lst=[i-avg for i in nums]
        # pointer=0
        # for i in range(1,n-k+1):
        #     laps=i-pointer
        #     if laps<k:
        #         s1=sum(lst[pointer:pointer+laps])
        #         s2=sum(lst[i+k-laps:i+k])
        #         if s1<s2:
        #             pointer=i
        #     else:
        #         s1=sum(lst[pointer:pointer+k])
        #         s2=sum(lst[i:i+k])
        #         if s1<s2:
        #             pointer=i
        # return sum(nums[pointer:pointer+k])/k

        # n=len(nums)
        # if n==k:
        #     return sum(nums)/k
        # else:
        #     return max(FindMaxAverage(nums[:n-1],k),sum(nums[-k:n])/k)
        
        n=len(nums)
        result=sum(nums[:k])
        s=result
        for i in range(k,n):
            s+=nums[i]-nums[i-k]
            if s>result:
                result=s
        return result/k

print(FindMaxAverage([0,4,0,3,2],1))
print(FindMaxAverage([1,12,-5,-6,50,3],4))
print(FindMaxAverage([5,1],1))