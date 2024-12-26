#
# @lc app=leetcode id=2413 lang=python
#
# [2413] Smallest Even Multiple
#

# @lc code=start
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2 != 0:
            return 2*n
        else:
            return n
        
# @lc code=end

