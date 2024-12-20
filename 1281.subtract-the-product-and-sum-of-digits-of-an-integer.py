#
# @lc app=leetcode id=1281 lang=python
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOfDigits = 0
        productOfDigits = 1
        for digit in str(n):
            sumOfDigits += int(digit)
            productOfDigits *= int(digit)
        return productOfDigits - sumOfDigits
    
    
# @lc code=end

