def LongestSubarray(nums):
    # def consecutive(lst):
    #     result=0
    #     n=len(lst)
    #     count=0
    #     for i in range(n):
    #         if lst[i]!=0:
    #             count+=1
    #             if i==n-1:
    #                 result=max(result,count)
    #         else:
    #             result=max(result,count)
    #             count=0
    #     return result
    
    # result=0
    # n=len(nums)
    # for i in range(n):
    #     duplicate=nums.copy()
    #     duplicate.pop(i)
    #     length=consecutive(duplicate)
    #     if result<length:
    #         result=length
    
    # return result
    l=r=0
    n=len(nums)
    k=1
    for r in range(n):
        if nums[r]==0:
            k-=1
        if k<0:
            if nums[l]==0:
                k+=1
            l+=1
    return r-l











nums=[1,1,0,1]
nums=[0,1,1,1,0,1,1,0,1]
print(LongestSubarray(nums))