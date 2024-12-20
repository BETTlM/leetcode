#
# @lc app=leetcode id=1317 lang=python
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#

# @lc code=start
class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]
# @lc code=end

