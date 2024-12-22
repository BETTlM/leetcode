#
# @lc app=leetcode id=1491 lang=python
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary = sorted(salary)
        return sum(salary[1:-1]) / float(len(salary) - 2)
    
 

# @lc code=end

