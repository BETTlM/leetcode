#
# @lc app=leetcode id=1844 lang=python
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            else:
                res.append(chr(ord(s[i-1]) + int(s[i])))
        return ''.join(res)
        
# @lc code=end

