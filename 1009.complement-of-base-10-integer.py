#
# @lc app=leetcode id=1009 lang=python
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        obin = bin(n)[2::]
        newbin = ''
        for i in obin:
            if i == '1':
                newbin += '0'
            else:
                newbin += '1'
        newnum = int(newbin,2)
        return newnum
# @lc code=end

