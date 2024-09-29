#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for i in digits:
            num+=str(i)
        newnum = str(int(num)+1)
        digs = list(newnum)
        red=[]
        for i in digs:
            red.append(int(i))
        return red
# @lc code=end

