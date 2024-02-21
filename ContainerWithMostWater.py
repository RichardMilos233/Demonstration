def MaxArea(height):
        n=len(height)
        area=float('-inf')
        left=0
        right=n-1
        while left<right:
            length=right-left
            width=min(height[left],height[right])
            currentarea=length*width
            area=max(area,currentarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area

print(MaxArea([1,8,6,2,5,4,8,3,7]))