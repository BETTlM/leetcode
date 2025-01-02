#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeat = set()
        for i in nums:
            if i in repeat:
                return i
            else:
                repeat.add(i)
# @lc code=end

