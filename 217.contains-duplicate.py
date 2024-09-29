#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueElements = list(set(nums))
        if len(nums)==len(uniqueElements):
            return False
        else:
            return True
# @lc code=end

