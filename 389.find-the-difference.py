#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#
import collections
# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = collections.Counter(s)

        for c in t:
            if count[c] == 0:
                return c
            count[c] -= 1

# @lc code=end

