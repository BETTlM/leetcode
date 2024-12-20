#
# @lc app=leetcode id=1342 lang=python
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        if num == 0:
            return steps
        elif num == 1:
            return 1
        else:
            while num != 0:
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = num - 1
                steps += 1
            return steps
# @lc code=end

