#
# @lc app=leetcode id=2652 lang=python
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumofmultiples = 0
        for i in range(1,n +1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                sumofmultiples += i
        return sumofmultiples
        
# @lc code=end

