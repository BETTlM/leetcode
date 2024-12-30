#
# @lc app=leetcode id=2574 lang=python
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum = []
        for i in range(len(nums)):
            leftsum.append(sum(nums[:i]))
        rightsum = []
        for i in range(len(nums)):
            rightsum.append(sum(nums[i+1:]))
        return [abs(leftsum[i] - rightsum[i]) for i in range(len(nums))]
        
# @lc code=end

