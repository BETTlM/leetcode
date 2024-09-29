#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueElements = list(set(nums))
        for i in uniqueElements:
            if nums.count(i)>(len(nums)/2):
                return i
# @lc code=end

