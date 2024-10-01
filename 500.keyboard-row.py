#
# @lc app=leetcode id=500 lang=python
#
# [500] Keyboard Row
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        valid = []
        for j in words:
            i = j.lower()
            if i[0] in row1:
                r = row1
            elif i[0] in row2:
                r = row2
            elif i[0] in row3:
                r = row3
            status = True
            for letter in i:
                if letter in r:
                    pass
                else:
                    status = False
                    break
            if status is True:
                valid.append(j)
        return valid
# @lc code=end

