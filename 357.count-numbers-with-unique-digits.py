#
# @lc app=leetcode id=357 lang=python
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        vals = {0:1, 1:10, 2:91, 3:739, 4:5275, 5:32491, 6:168571, 7:712891, 8:2345851}

        return vals[n]
# @lc code=end

