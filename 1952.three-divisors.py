#
# @lc app=leetcode id=1952 lang=python
#
# [1952] Three Divisors
#

# @lc code=start
class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divisors = 0 
        for i in range(1, n+1):
            if n % i == 0:
                divisors += 1
                if divisors > 3:
                    return False
        return divisors == 3
        
# @lc code=end

