#
# @lc app=leetcode id=1945 lang=python
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        chardict = dict()
        for i in range(26):
            chardict[chr(i+97)] = str(i+1)
        num = ''.join(chardict[c] for c in s)
        return num

# @lc code=end

