#
# @lc app=leetcode id=1295 lang=python
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
# @lc code=end

