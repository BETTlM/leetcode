#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target<= nums[0]:
            return 0
        elif target> nums[-1]:
            return len(nums)
        elif target==nums[-1]:
            return len(nums)-1
        else:
            for i in range(len(nums)-1):
                if nums[i] < target and nums[i+1]>= target:
                    return i+1
# @lc code=end

