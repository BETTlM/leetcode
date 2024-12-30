#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # edge case
        if not nums:
            return 0

        # two pointers
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
        
# @lc code=end

