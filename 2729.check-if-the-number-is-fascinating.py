#
# @lc app=leetcode id=2729 lang=python
#
# [2729] Check if The Number is Fascinating
#

# @lc code=start
class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return set(str(n) + str(n*2) + str(n*3)) == set('123456789') and len(str(n)) == len(set(str(n)))
        
# @lc code=end

