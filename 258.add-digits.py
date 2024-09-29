#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        n = str(num)
        sum = 0
        while True:
            for i in n:
                sum = sum + int(i)
            if sum<10:
                return sum
            else:
                n = str(sum)
                sum = 0

# @lc code=end

