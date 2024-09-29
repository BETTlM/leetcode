#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#

# @lc code=start
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 0
        while True:
            if 3**power == n:
                return True
            elif 3**power>n:
                return False
            power = power + 1        
# @lc code=end

