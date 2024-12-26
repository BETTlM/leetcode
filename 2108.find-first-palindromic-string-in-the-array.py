#
# @lc app=leetcode id=2108 lang=python
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def palindome(s):
            return s == s[::-1]
        for word in words:
            if palindome(word):
                return word
        else:
            return ""
# @lc code=end

