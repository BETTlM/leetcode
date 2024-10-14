#
# @lc app=leetcode id=728 lang=python
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sdn = []
        for i in range(left,right+1):
            num = str(i)
            status = True
            for j in num:
                if j == '0':
                    status = False
                elif i%int(j)!=0:
                    status = False
                
            if status is True:
                sdn.append(i)
        return sdn
# @lc code=end

