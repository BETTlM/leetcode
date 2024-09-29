#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 0 
        while True:
            if 4**power == n:
                return True
            elif 4**power>n:
                return False
            power = power + 1
            
        
# @lc code=end

