#
# @lc app=leetcode id=1507 lang=python
#
# [1507] Reformat Date
#

# @lc code=start
class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        date = date.split()
        day = date[0][:-2]
        if len(day) == 1:
            day = '0' + day
        month = date[1]
        month_dict = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        month = month_dict[month]
        year = date[2]
        return year + '-' + month + '-' + day
    
# @lc code=end

