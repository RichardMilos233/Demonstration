def LongestOnes(nums,k):
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
        # if k==0:
        #     return consecutive(nums)
        
        # n=len(nums)
        # z=[]
        # count=0
        # for i in range(n):
        #     if nums[i]==0:
        #         nums[i]=2
        #         z+=[i]
        #         count+=1
        #     if count==k:
        #         break
        # print(nums)
        
        
        # length=consecutive(nums)
        # while 1:
        #     left=z[0]
        #     nums[left]=0
        #     z.pop(0)
        #     right=z[-1]
        #     flag=0
        #     for i in range(right+1,n):
        #         if nums[i]==0:
        #             nums[i]=2
        #             z+=[i]
        #             flag=1
        #             break
        #     if flag==0:
        #         break
        #     print(nums)
        #     length=max(length,consecutive(nums))
        # return length
        def leftright(lst,left,right):
            n=len(lst)
            while lst[left]!=0:
                if left==0:
                    break
                left-=1
            if lst[left]==0:
                left+=1
            
            while lst[right]!=0:
                if right==n-1:
                    break
                right+=1
            if lst[right]==0:
                right-=1
            
            return right-left+1
        
        def consecutive(lst):
            result=0
            n=len(lst)
            count=0
            for i in range(n):
                if lst[i]!=0:
                    count+=1
                    if i==n-1:
                        result=max(result,count)
                else:
                    result=max(result,count)
                    count=0
            return result
        if k==0:
            return consecutive(nums)

        n=len(nums)
        z=[]
        count=0
        for i in range(n):
            if nums[i]==0:
                nums[i]=2
                z+=[i]
                count+=1
            if count==k:
                break

        length=consecutive(nums)
        while 1:
            left=z[0]
            nums[left]=0
            right=z[-1]
            z.pop(0)
            flag=0
            for i in range(right+1,n):
                if nums[i]==0:
                    nums[i]=2
                    z+=[i]
                    flag=1
                    break
            if flag==0:
                break
            length=max(length,leftright(nums,z[0],z[-1]))
        return length
    


print(LongestOnes([0,0,0,1],4))
print(LongestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(LongestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(LongestOnes([0],1))