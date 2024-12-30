#
# @lc app=leetcode id=2710 lang=python
#
# [2710] Remove Trailing Zeros From a String
#

# @lc code=start
class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        while num[-1] == '0':
            num = num[:-1]
        return num
        # @lc code=end

