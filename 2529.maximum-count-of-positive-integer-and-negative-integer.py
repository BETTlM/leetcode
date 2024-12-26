#
# @lc app=leetcode id=2529 lang=python
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negcount = 0
        poscount = 0
        for num in nums:
            if num < 0:
                negcount += 1
            elif num > 0:
                poscount += 1
        return max(negcount, poscount)
# @lc code=end

