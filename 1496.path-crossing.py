#
# @lc app=leetcode id=1496 lang=python
#
# [1496] Path Crossing
#

# @lc code=start
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = []
        x,y = 0,0
        visited.append((x,y))
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            if (x,y) in visited:
                return True
            visited.append((x,y))
        return False
# @lc code=end

