#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        numa = int(a,2)
        numb = int(b,2)
        su = numa + numb
        sus = bin(su)[2::]
        return sus        
# @lc code=end

