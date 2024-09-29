#
# @lc app=leetcode id=476 lang=python
#
# [476] Number Complement
#

# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        binum = bin(num)[2::]
        retbin = ''
        for i in binum:
            if i=='1':
                retbin+='0'
            else:
                retbin+='1'
        
        return int(retbin,2)
# @lc code=end

