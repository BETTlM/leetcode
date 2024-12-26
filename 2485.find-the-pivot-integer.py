#
# @lc app=leetcode id=2485 lang=python
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        pivot = False
        for i in range(1, n):
           if sum(range(1, i)) == sum(range(i+1, n+1)):
               pivot = True
               break
        return i if pivot else -1
    
# @lc code=end

