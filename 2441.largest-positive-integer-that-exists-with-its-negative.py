#
# @lc app=leetcode id=2441 lang=python
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -1
        for i in list(set(nums)):
            if -i in nums:
                largest = max(largest, i)
        return largest
# @lc code=end

