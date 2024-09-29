#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
import collections
# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = collections.Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
            
# @lc code=end

