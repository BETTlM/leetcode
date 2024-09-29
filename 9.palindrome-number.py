#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x<10:
            return True
        else:
            retx = str(x)[::-1]
            if retx == str(x):
                return True
            else:
                return False
            
        
# @lc code=end

