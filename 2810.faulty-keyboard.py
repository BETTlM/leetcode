#
# @lc app=leetcode id=2810 lang=python
#
# [2810] Faulty Keyboard
#

# @lc code=start
class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        retstr = ''
        for i in s:
            if i != 'i':
                retstr += i
            else:
                retstr = retstr[::-1]
        return retstr
        
# @lc code=end

