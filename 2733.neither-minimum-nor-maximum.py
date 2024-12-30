#
# @lc app=leetcode id=2733 lang=python
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        nums.sort()
        unique_nums = set(nums)
        if len(unique_nums) == 1:
            return -1
        return list(unique_nums)[-2]
# @lc code=end

