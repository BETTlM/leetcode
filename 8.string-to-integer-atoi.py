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
        s = s.strip()
        if not s:
            return 0
        
        if s[0] =='-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        digits = ''
        for i in s:
            if i.isdigit():
                digits += i
            else:
                break
        if len(digits) == 0:
            return 0
       

        result = sign * int(digits)
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result


        
        
# @lc code=end

