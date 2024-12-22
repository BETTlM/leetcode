#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2**31 or x > 2**31 - 1:
            return 0
        if x == 0: 
            return 0
        if x < 0:
            return -1 * self.reverse(-1 * x)
        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x
    
# @lc code=end

