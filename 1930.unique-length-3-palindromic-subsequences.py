#
# @lc app=leetcode id=1930 lang=python
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        palisubs = set()
        for i in range(len(s)-2):
            for j in range(i+1,len(s)-1):
                for k in range(j+1,len(s)):
                    cons = s[i]+s[j]+s[k]
                    if s[i] == s[k] and cons not in palisubs:
                        palisubs.add(cons)
        return len(palisubs)
        
# @lc code=end

