#
# @lc app=leetcode id=2843 lang=python
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for i in range(low, high+1):
            if len(str(i)) == 1:
                continue
            elif len(str(i)) != 2:
                continue
            else:
                mid = len(str(i))//2
                lsum = rsum = 0
                for j in range(mid):
                    lsum += int(str(i)[j])
                    rsum += int(str(i)[len(str(i))-1-j])
                if lsum == rsum:
                    count += 1
        return count
        
# @lc code=end

