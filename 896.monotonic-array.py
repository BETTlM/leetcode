#
# @lc app=leetcode id=896 lang=python
#
# [896] Monotonic Array
#

# @lc code=start
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        asc = list(sorted(nums))
        desc = asc[::-1]
        if asc == nums or desc == nums:
            return True
        return False
        
# @lc code=end

