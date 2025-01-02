#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        length = len(nums)
        for i in range(0,length):
            if i % 2 == 0:
                sum1 += nums[i]
            else:
                sum2 += nums[i]
        return max(sum1,sum2)
# @lc code=end

