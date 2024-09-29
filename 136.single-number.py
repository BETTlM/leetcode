#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = list(set(nums))
        for i in digits:
            if nums.count(i) == 1:
                return i
# @lc code=end

