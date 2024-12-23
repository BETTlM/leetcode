#
# @lc app=leetcode id=1935 lang=python
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split()
        broken = set(brokenLetters)
        count = 0
        for word in words:
            if not any(c in broken for c in word):
                count += 1
        return count
# @lc code=end

