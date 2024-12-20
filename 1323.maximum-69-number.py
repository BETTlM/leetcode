#
# @lc app=leetcode id=1323 lang=python
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        if '6' in num_str:
            num_str = num_str.replace('6', '9', 1)
        return int(num_str)
