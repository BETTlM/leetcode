#
# @lc app=leetcode id=1450 lang=python
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count = 0 
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count
        
# @lc code=end

