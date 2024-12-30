#
# @lc app=leetcode id=2544 lang=python
#
# [2544] Alternating Digit Sum
#

# @lc code=start
class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sign = 1
        sum = 0 
        for i in str(n):
            sum += int(i) * sign
            sign *= -1
        return sum
        
# @lc code=end

