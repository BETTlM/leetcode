#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#

# @lc code=start
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        bits = []
        for i in range(n+1):
            numb = bin(i)
            digcount = numb.count('1')
            bits.append(digcount)
        return bits
# @lc code=end

