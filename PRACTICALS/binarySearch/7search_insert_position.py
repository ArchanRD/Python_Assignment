def searchInsert(nums, target):
    if target in nums:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
    else:
        if target < nums[0]:
            return 0
        else:
            for i in range(len(nums)-1, -1, -1):
                if target > nums[i]:
                    return i+1

nums1 = [1,3,5,6]
nums2 = [1,3,5,6]
print(searchInsert([1,3,5,6], 2))