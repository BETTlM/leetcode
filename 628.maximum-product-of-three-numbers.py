#
# @lc app=leetcode id=628 lang=python
#
# [628] Maximum Product of Three Numbers
#
import math
# @lc code=start
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[0] * nums[1],
                    nums[-1] * nums[-2] * nums[-3])
# @lc code=end

