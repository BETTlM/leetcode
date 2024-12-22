#
# @lc app=leetcode id=1512 lang=python
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goodpair = 0 
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    goodpair += 1
        return goodpair
# @lc code=end

