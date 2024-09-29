#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)[2::]
        counts = num.count('1')
        return counts
# @lc code=end

