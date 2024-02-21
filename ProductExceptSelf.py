def ProductExceptSelf(nums):
    pi=1
    n=len(nums)
    for i in nums:
        pi*=i
    result=[]
    if pi==0:
        for i in range(n):
            if nums[i]==0:
                product=1
                for j in nums[0:i]+nums[i+1:]:
                    product*=j
                result.append(product)
            else:
                result.append(0)
    else:
        for i in nums:
            result.append(pi//i)
    return result

print(ProductExceptSelf([-1,1,0,-3,3]))