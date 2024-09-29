#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = list('aeiouAEIOU')
        existingvowels = []
        retstr = ''
        for i in s:
            if i in vowels:
                existingvowels.append(i)
        for i in s:
            if i not in vowels:
                retstr = retstr + i
            else:
                retstr = retstr + existingvowels.pop()
        return retstr
# @lc code=end

