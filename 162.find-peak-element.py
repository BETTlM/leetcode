#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        change = False
        index = len(nums) - 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                index = i
                change = True
        if index == len(nums) - 1 or nums[index] > nums[index + 1]:
            if change:
                return index
            else:
                return 0
        else:
            return len(nums) - 1
# @lc code=end

