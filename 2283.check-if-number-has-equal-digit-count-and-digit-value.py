#
# @lc app=leetcode id=2283 lang=python
#
# [2283] Check if Number Has Equal Digit Count and Digit Value
#

# @lc code=start
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            if num.count(num[i]) != int(num[i]):
                return False
        return True
        
# @lc code=end

