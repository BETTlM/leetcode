#
# @lc app=leetcode id=1051 lang=python
#
# [1051] Height Checker
#

# @lc code=start
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = list(sorted(heights))
        count = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1
        return count
        
# @lc code=end

