def maxOperations(nums, k):
        nums.sort()
        left=0
        pairs=0
        right=len(nums)-1
        while True:
            if left>=right:
                 break
            if nums[left]+nums[right]==k:
                pairs+=1
                right-=1
                left+=1
            if nums[left]+nums[right]<k:
                left+=1
            if nums[left]+nums[right]>k:
                right-=1
        return pairs


print(maxOperations([3,5,1,5],2))
