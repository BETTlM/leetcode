#
# @lc app=leetcode id=1436 lang=python
#
# [1436] Destination City
#

# @lc code=start
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        output = paths[0][1]
        while True:
            for i in paths:
                if i[0] == output:
                    output = i[1]
                    break
            else:
                break
        return output
    
# @lc code=end

