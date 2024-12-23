#
# @lc app=leetcode id=1837 lang=python
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        while n:
            res += n % k
            n //= k
        return res
        
# @lc code=end

