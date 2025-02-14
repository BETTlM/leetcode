#
# @lc app=leetcode id=2017 lang=python
#
# [2017] Grid Game
#

# @lc code=start
class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        original_path = sum(grid[0])
        bottom_path = 0
        answer = float('inf')

        for i in range(len(grid[0])):
            original_path -= grid[0][i]
            answer = min(answer, max(original_path, bottom_path))
            bottom_path += grid[1][i]
        
        return answer
        
        
        # @lc code=end

