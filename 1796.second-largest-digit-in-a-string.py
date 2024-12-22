#
# @lc app=leetcode id=1796 lang=python
#
# [1796] Second Largest Digit in a String
#

# @lc code=start
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        for i in s:
            if i.isdigit():
                nums.append(int(i))
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 2:
            return -1
        return nums[-2]
    
        
# @lc code=end

