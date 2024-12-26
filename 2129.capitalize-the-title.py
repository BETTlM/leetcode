#
# @lc app=leetcode id=2129 lang=python
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        output = ''
        for i in title.split():
            if len(i) < 3:
                output += i.lower() + ' '
            else:
                output += i.capitalize() + ' '
        return output.strip()
# @lc code=end

