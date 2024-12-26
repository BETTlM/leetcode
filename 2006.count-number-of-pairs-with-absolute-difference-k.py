#
# @lc app=leetcode id=2006 lang=python
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
    
# @lc code=end

