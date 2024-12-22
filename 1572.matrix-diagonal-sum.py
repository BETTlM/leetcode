#
# @lc app=leetcode id=1572 lang=python
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat) - i - 1]
        if len(mat) % 2 != 0:
            sum -= mat[len(mat) // 2][len(mat) // 2]
        return sum
# @lc code=end

