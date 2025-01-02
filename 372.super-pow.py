#
# @lc app=leetcode id=372 lang=python
#
# [372] Super Pow
#

# @lc code=start
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        intb = ''
        for i in b:
            intb += str(i)
        intb = int(intb)
        def mod_exp(x, y, mod):
            result = 1
            x = x % mod
            while y > 0:
                if (y % 2) == 1:
                    result = (result * x) % mod
                y = y >> 1
                x = (x * x) % mod
            return result

        return mod_exp(a, intb, 1337)
# @lc code=end

