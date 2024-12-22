#
# @lc app=leetcode id=1556 lang=python
#
# [1556] Thousand Separator
#

# @lc code=start
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return '0'
        res = ''
        count = 0
        while n > 0:
            if count == 3:
                res = '.' + res
                count = 0
            res = str(n % 10) + res
            n = n // 10
            count += 1
        return res
        
# @lc code=end

