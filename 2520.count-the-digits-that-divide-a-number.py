#
# @lc app=leetcode id=2520 lang=python
#
# [2520] Count the Digits That Divide a Number
#

# @lc code=start
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0 
        for i in str(num):
            if num%int(i) == 0:
                cnt += 1

        return cnt
        
# @lc code=end

