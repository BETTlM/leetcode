#
# @lc app=leetcode id=2119 lang=python
#
# [2119] A Number After a Double Reversal
#

# @lc code=start
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        rev1 = int(str(num)[::-1])
        rev2 = int(str(rev1)[::-1])
        return num == rev2
# @lc code=end

