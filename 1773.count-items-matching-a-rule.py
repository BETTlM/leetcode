#
# @lc app=leetcode id=1773 lang=python
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        key = {"type": 0, "color": 1, "name": 2}
        return sum([item[key[ruleKey]] == ruleValue for item in items])
        
# @lc code=end

