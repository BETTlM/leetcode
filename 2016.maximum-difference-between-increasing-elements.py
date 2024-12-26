#
# @lc app=leetcode id=2016 lang=python
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdif = 0
        change = False
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] >maxdif:
                    maxdif = nums[j] - nums[i]
                    change = True
        if change:
            return maxdif
        return -1
    
# @lc code=end

