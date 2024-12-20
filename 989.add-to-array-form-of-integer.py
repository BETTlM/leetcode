#
# @lc app=leetcode id=989 lang=python
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        originalNumber = ''
        for i in num:
            originalNumber += str(i)
        newNumber = str(int(originalNumber)+k)
        returnList = []
        for i in newNumber:
            returnList.append(int(i))
        return returnList
# @lc code=end

