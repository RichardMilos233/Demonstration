def SingleNumber(nums):
        if len(nums)==1:
            return nums[0]
        nums.sort()
        i=0
        while i <len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[-1]


print(SingleNumber([4,3,4,1,2,1,2]))