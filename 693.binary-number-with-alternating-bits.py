#
# @lc app=leetcode id=693 lang=python
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)
        if n == 1:
            return True
        if len(binary)<4:
            return False
        
        elif '11' in binary or '00' in binary:
            return False
        
        else:
            return True
# @lc code=end

