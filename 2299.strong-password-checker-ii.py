#
# @lc app=leetcode id=2299 lang=python
#
# [2299] Strong Password Checker II
#

# @lc code=start
class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        digit = False
        upper = False
        lower = False
        special = False
        adjacent = False
        if len(password) < 6:
            return False
        for i in range(len(password)):
            if password[i].isdigit():
                digit = True
            if password[i].isupper():
                upper = True
            if password[i].islower():
                lower = True
            if not password[i].isalnum():
                special = True
            if i > 0 and password[i] == password[i-1]:
                adjacent = True
        return digit and upper and lower and special and not adjacent
# @lc code=end

