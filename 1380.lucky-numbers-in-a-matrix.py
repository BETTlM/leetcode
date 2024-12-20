#
# @lc app=leetcode id=1380 lang=python
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_mins = [min(row) for row in matrix]
        col_maxs = [max(col) for col in zip(*matrix)]
        
        count = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                    count.append(matrix[i][j])
        return count

        
# @lc code=end

