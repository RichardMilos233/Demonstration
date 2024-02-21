def MoveZeros(nums):
    i=0
    j=len(nums)
    count=0
    result=[]
    for i in range(j):
        if nums[i]==0:
            count+=1
        else:
            result.append(nums[i])
    for j in range(count):
        result.append(0)
    nums=result
    return nums

print(MoveZeros([0,3,0,4]))
