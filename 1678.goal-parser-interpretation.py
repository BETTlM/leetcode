#
# @lc app=leetcode id=1678 lang=python
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace('()', 'o').replace('(al)', 'al')
# @lc code=end

