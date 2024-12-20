#
# @lc app=leetcode id=1351 lang=python
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        negcount = 0
        for i in grid:
            for j in i:
                if j < 0:
                    negcount += 1
        return negcount
# @lc code=end

