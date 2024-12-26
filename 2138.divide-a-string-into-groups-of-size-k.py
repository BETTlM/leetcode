#
# @lc app=leetcode id=2138 lang=python
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        remx = len(s) % k
        if remx:
            s += fill * (k - remx)
        output = []
        for i in range(0, len(s), k):
            output.append(s[i:i+k])
        return output
    
# @lc code=end

