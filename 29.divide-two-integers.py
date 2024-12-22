#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int

        """
        quotioent = 0
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotioent += i
                i <<= 1
                temp <<= 1
        if sign < 0:
            quotioent = -quotioent  
        return min(max(-2**31, quotioent), 2**31-1)
    
        
# @lc code=end

