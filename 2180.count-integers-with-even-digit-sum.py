#
# @lc app=leetcode id=2180 lang=python
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def isdigitsumeven(n):
            s = 0 
            for i in str(n):
                s += int(i)
            if s%2 == 0:
                return True
            else:
                return False
        count = 0 
        for i in range(2, num+1):
                if isdigitsumeven(i):
                    count += 1
        return count
# @lc code=end

