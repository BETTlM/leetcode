#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        if s[0] == '-':
            sign -= 2
        s = s[1:]
        if not s:
            return 0
        n = 0 
        for i in s:
            if i.isdigit():
                n = n * 10 + int(i)
            else:
                break
        n = n * sign
        if n > 2**31 - 1:
            return 2**31 - 1
        if n < -2**31:
            return -2**31
        return n
    
        
# @lc code=end

