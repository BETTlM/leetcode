#
# @lc app=leetcode id=1748 lang=python
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        for i in nums:
            if nums.count(i) == 1:
                unique.append(i)
        return sum(unique)
        
# @lc code=end

