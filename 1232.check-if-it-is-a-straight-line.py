#
# @lc app=leetcode id=1232 lang=python
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        dx1 = x2 - x1
        dy1 = y2 - y1
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            dx2 = x - x1
            dy2 = y - y1
            if dx1 * dy2 != dy1 * dx2:
                return False
        return True

# @lc code=end

