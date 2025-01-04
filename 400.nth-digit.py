#
# @lc app=leetcode id=400 lang=python
#
# [400] Nth Digit
#

# @lc code=start
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_length = 1
        count = 9
        start = 1
        
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        start += (n - 1) // digit_length
        s = str(start)
        return int(s[(n - 1) % digit_length])
        
# @lc code=end

