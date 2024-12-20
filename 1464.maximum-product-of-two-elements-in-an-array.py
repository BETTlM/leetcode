#
# @lc app=leetcode id=1464 lang=python
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] - 1) * (nums[j] - 1) > max:
                    max = (nums[i] - 1) * (nums[j] - 1)
        return max
        
# @lc code=end

