#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        numsss = set(nums)
        for i in numsss:
            if nums.count(i) == 1:
                return i
        return -1
        
# @lc code=end

