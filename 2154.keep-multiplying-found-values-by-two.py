#
# @lc app=leetcode id=2154 lang=python
#
# [2154] Keep Multiplying Found Values by Two
#

# @lc code=start
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        if original not in nums:
            return original
        while True:
            original *= 2
            if original not in nums:
                return original
            
            
        
# @lc code=end

