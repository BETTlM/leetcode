#
# @lc app=leetcode id=1925 lang=python
#
# [1925] Count Square Sum Triples
#

# @lc code=start
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                c = (a**2 + b**2)**0.5
                if c.is_integer() and c <= n:
                    count += 2 if a != b else 1
        return count
        
# @lc code=end

