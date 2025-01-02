#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n-1)
        fact = factorial(n)
        count = 0
        s = str(fact)
        while s[-1] == '0':
            count += 1
            s = s[:-1]
        return count
# @lc code=end

