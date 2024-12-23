#
# @lc app=leetcode id=1903 lang=python
#
# [1903] Largest Odd Number in String
#

# @lc code=start
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        odd = []
        for i in str(num):
            if int(i)%2 != 0:
                odd.append(int(i))
        if not odd:
            return ""
        else:
            return str(max(odd))
    
        
# @lc code=end

