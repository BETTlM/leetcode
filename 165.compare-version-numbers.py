#
# @lc app=leetcode id=165 lang=python
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(max(len(v1), len(v2))):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        return 0
        
# @lc code=end

