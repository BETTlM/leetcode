#
# @lc app=leetcode id=1822 lang=python
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        negative = 1
        for num in nums:
            if num < 0:
                negative *= -1
        return negative
    
# @lc code=end

