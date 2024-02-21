def IncreasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    for n in nums:
        if n<first:
            first=n
        if first<n<second:
            second=n
        if first<second<n:
            return True
    return False



