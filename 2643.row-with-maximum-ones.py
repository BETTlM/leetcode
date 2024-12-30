#
# @lc app=leetcode id=2643 lang=python
#
# [2643] Row With Maximum Ones
#

# @lc code=start
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max = 0
        row = 0
        for i in range(len(mat)):
            if mat[i].count(1) > max:
                max = mat[i].count(1)
                row = i
        return [row, max]
# @lc code=end

