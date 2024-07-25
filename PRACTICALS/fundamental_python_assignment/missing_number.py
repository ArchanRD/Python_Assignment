# leetcode problem: https://leetcode.com/problems/missing-number/description/

"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        while length >= 0:
            if length not in nums:
                return length
            length -= 1

nums = [3,2,0]
sol = Solution()
missing_num = sol.missingNumber(nums)
print(missing_num)