#
# @lc app=leetcode id=2270 lang=python
#
# [2270] Number of Ways to Split Array
#

# @lc code=start
class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ways = 0
        total_sum = sum(nums)
        prefix_sum = 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                ways += 1
        return ways
        
# @lc code=end

