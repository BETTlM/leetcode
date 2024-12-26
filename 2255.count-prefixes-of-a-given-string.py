#
# @lc app=leetcode id=2255 lang=python
#
# [2255] Count Prefixes of a Given String
#

# @lc code=start
class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0 
        for i in words:
            if s.startswith(i):
                count += 1
        return count
        
# @lc code=end

