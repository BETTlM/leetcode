#
# @lc app=leetcode id=1736 lang=python
#
# [1736] Latest Time by Replacing Hidden Digits
#

# @lc code=start
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hours = time.split(":")[0]
        minutes = time.split(":")[1]
        if '?' in hours:
            if hours[0] == '?':
                if hours[1] == '?':
                    hours = "23"
                elif int(hours[1]) < 4:
                    hours = "2" + hours[1]
                else:
                    hours = "1" + hours[1]
            elif hours[1] == '?':
                if int(hours[0]) < 2:
                    hours = hours[0] + "9"
                else:
                    hours = hours[0] + "3"
        if '?' in minutes:
            if minutes[0] == '?':
                minutes = "5" + minutes[1]
            if minutes[1] == '?':
                minutes = minutes[0] + "9"
        return hours + ":" + minutes
        
# @lc code=end

