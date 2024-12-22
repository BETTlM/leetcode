#
# @lc app=leetcode id=1523 lang=python
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - low // 2
        
# @lc code=end

