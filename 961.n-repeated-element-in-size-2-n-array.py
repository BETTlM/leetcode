#
# @lc app=leetcode id=961 lang=python
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        for i in list(set(nums)):
            if nums.count(i) == n:
                return i
        
# @lc code=end

