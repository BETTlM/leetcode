#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        """
        if len(nums) == 0:
            return 0
        maxprod = result = nums[0]
        for i in range(1, len(nums)):
            maxprod = max(nums[i], maxprod * nums[i])
            result = max(result, maxprod)
        return result
     
