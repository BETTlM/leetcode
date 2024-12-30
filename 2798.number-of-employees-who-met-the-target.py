#
# @lc app=leetcode id=2798 lang=python
#
# [2798] Number of Employees Who Met the Target
#

# @lc code=start
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        nums = 0
        for i in hours:
            if i >= target:
                nums += 1
        return nums
        
# @lc code=end

