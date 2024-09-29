#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 0
        while True:
            if n*n == num:
                return True
            elif n*n>num:
                return False
            n=n+1
        
# @lc code=end

