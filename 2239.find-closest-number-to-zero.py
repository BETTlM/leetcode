#
# @lc app=leetcode id=2239 lang=python
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distance = float('inf')
        closest = None
        for num in nums:
            if abs(num) < distance:
                distance = abs(num)
                closest = num
            elif abs(num) == distance:
                closest = max(closest, num)
        return closest
# @lc code=end

