#
# @lc app=leetcode id=1614 lang=python
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxdepths = []
        for i in range(len(s)):
            depth = maxdepths[-1] if maxdepths else 0
            if s[i] == '(':
                depth += 1
            elif s[i] == ')':
                depth -= 1
            maxdepths.append(depth)
        return max(maxdepths)
    
        
# @lc code=end

