#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if target in i:
                return True
        return False
# @lc code=end

