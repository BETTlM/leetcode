#
# @lc app=leetcode id=201 lang=python
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        a = 1
        while left != right:
            left >>= 1
            right >>= 1
            a <<= 1
        return left * a
# @lc code=end

