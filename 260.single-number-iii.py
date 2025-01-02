#
# @lc app=leetcode id=260 lang=python
#
# [260] Single Number III
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        once = []
        for i in nums:
            if i in once:
                once.remove(i)
            else:
                once.append(i)
        return once
        
# @lc code=end

