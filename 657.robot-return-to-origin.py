#
# @lc app=leetcode id=657 lang=python
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        xcord = 0
        ycord = 0
        for i in moves:
            if i == 'U':
                xcord += 1
            elif i == 'D':
                xcord -= 1
            elif i == 'L':
                ycord += 1
            else:
                ycord -= 1
        if xcord == 0 and ycord == 0:
            return True
        return False
# @lc code=end

