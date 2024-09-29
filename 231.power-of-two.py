#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 0
        while True:
            if 2**power == n:
                return True
            elif 2**power > n:
                return False
            else:
                power += 1
        
# @lc code=end

